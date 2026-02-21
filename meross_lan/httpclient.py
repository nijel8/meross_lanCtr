"""
    Implementation for an async (aiohttp.ClientSession) http client
    for Meross devices.
"""

from __future__ import annotations
from json import (
    dumps as json_dumps,
    loads as json_loads,
)
import asyncio
import async_timeout
import aiohttp
from yarl import URL
from uuid import uuid4
from hashlib import md5
from time import time

from . import const as mc

class MerossProtocolError(Exception):
    """
    signal a protocol error like:
    - missing header keys
    - application layer ERROR(s)

    reason is an error payload (dict) if the protocol is formally correct
    and the device replied us with "method" : "ERROR"
    and "payload" : { "error": { "code": (int), "detail": (str) } }
    in a more general case it could be the exception raised by accessing missing
    fields or a "signature error" in our validation
    """
    def __init__(self, reason):
        super().__init__()
        self.reason = reason


class MerossKeyError(MerossProtocolError):
    """
    signal a protocol key error (wrong key)
    reported by device
    """

class MerossHttpClient:

    timeout = 5 # total timeout will be 1+2+4: check relaxation algorithm

    def __init__(
        self,
        host: str,
        key: str,
        session: aiohttp.ClientSession | None = None
    ):
        """
        host: device ip
        key: device key used for signing
        session: the shared session to use or None to create a dedicated one
        """
        self._host = host
        self._requesturl = URL(f"http://{host}/config")
        self.key = key
        self._session = session or aiohttp.ClientSession()

    def build_payload(
        self,
        namespace:str,
        method:str,
        payload:dict,
        key:KeyType,
        from_:str,
        messageid:str | None = None
    ) -> dict:
        if isinstance(key, dict):
            key[mc.KEY_NAMESPACE] = namespace
            key[mc.KEY_METHOD] = method
            key[mc.KEY_PAYLOADVERSION] = 1
            key[mc.KEY_FROM] = from_
            return {
                mc.KEY_HEADER: key,
                mc.KEY_PAYLOAD: payload
            }
        else:
            if messageid is None:
                messageid = uuid4().hex
            timestamp = int(time())
            return {
                mc.KEY_HEADER: {
                    mc.KEY_MESSAGEID: messageid,
                    mc.KEY_NAMESPACE: namespace,
                    mc.KEY_METHOD: method,
                    mc.KEY_PAYLOADVERSION: 1,
                    mc.KEY_FROM: from_,
                    mc.KEY_TIMESTAMP: timestamp,
                    mc.KEY_TIMESTAMPMS: 0,
                    mc.KEY_SIGN: md5((messageid + (key or "") +
                        str(timestamp)).encode('utf-8')).hexdigest()
                },
                mc.KEY_PAYLOAD: payload
            }

    async def async_request_raw(self, request: dict) -> dict:
        timeout = 1
        debugid = None
        try:
            request_data = json_dumps(request)
            # since device HTTP service sometimes timeouts with no apparent
            # reason we're using an increasing timeout loop to try recover
            # when this timeout is transient
            while True:
                try:
                    with async_timeout.timeout(timeout):
                        response = await self._session.post(
                            url=self._requesturl,
                            data=request_data
                        )
                    break
                except asyncio.TimeoutError as e:
                    if timeout < self.timeout:
                        timeout = timeout * 2
                    else:
                        raise e

            response.raise_for_status()
            text_body = await response.text()
            json_body:dict = json_loads(text_body)
        except Exception as e:
            raise e

        return json_body

    async def async_request_strict(self, namespace: str, method: str, payload: dict) -> dict:
        """
        check the protocol layer is correct and no protocol ERROR
        is being reported
        """
        key = self.key
        request: dict = self.build_payload(
            namespace, method, payload, key, mc.MANUFACTURER)
        response = await self.async_request_raw(request)
        try:
            r_header: dict = response[mc.KEY_HEADER]
            r_namespace: str = r_header[mc.KEY_NAMESPACE]
            r_method: str = r_header[mc.KEY_METHOD]
            r_payload: dict = response[mc.KEY_PAYLOAD]
        except Exception as e:
            raise MerossProtocolError(e) from e

        if r_method == mc.METHOD_ERROR:
            if r_payload.get(mc.KEY_ERROR, {}).get(mc.KEY_CODE) == mc.ERROR_INVALIDKEY:
                raise MerossKeyError(r_payload)
            else:
                raise MerossProtocolError(r_payload)

        return response
