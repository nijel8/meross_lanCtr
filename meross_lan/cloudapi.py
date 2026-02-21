from uuid import uuid4
from hashlib import md5
from base64 import b64encode
from time import time
from json import dumps as json_dumps
import async_timeout
import aiohttp
import json
import sys

import const as mc

async def async_merossapi_post(
    url_or_path: str,
    data: dict,
    session: aiohttp.ClientSession
) -> dict:
    try:
        timestamp = int(time() * 1000)
        nonce = uuid4().hex
        params = json.dumps(data, ensure_ascii=False)
        params = b64encode(params.encode("utf-8")).decode("utf-8")
        sign = md5(
            "".join(("23x17ahWarFH6w29", str(timestamp), nonce, params)).encode("utf-8")
        ).hexdigest()
        headers = None
        json_request = {
            mc.KEY_TIMESTAMP: timestamp,
            mc.KEY_NONCE: nonce,
            mc.KEY_PARAMS: params,
            mc.KEY_SIGN: sign,
        }
        async with async_timeout.timeout(10):
            http_response = await session.post(
                url=url_or_path,
                json=json_request,
                headers=headers,
            )
            http_response.raise_for_status()

        text_response = await http_response.text()
        json_response = json.loads(text_response)
        if not isinstance(json_response, dict):
            raise Exception("HTTP response is not a json dictionary")

        return json_response
    except Exception as exception:
        raise exception

async def async_get_cloud_key(
        username: str,
        password: str,
        session: aiohttp.ClientSession
    ) -> str:
    response = await async_merossapi_post(
        mc.MEROSS_API_V1_URL + mc.MEROSS_API_SIGNIN_PATH,
        {"email": username, "password": password},
        session=session
    )
    try:
        data = response[mc.KEY_DATA]
        if data:
            key = data[mc.KEY_KEY]
            if key:
                # everything good:
                # kindly invalidate login token so to not exhaust our pool...
                try:
                    await async_merossapi_post(
                        mc.MEROSS_API_LOGOUT_PATH,
                        {},
                        data[mc.KEY_TOKEN],
                        session=session
                    )
                except:
                    pass# don't care if any failure here: we have the key anyway
                return key
    except:
        print("==============ERROR: cloud response:=================")
        print(response)
        print("=====================================================")
        pass
