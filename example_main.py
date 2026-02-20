'''
 Toggle Meross mts960 smart socket thermostat device ON/OFF
 making sure operating in HEAT mode
'''
import subprocess
import asyncio

from httpclient import MerossHttpClient
import const as mc

async def main():
    # Create local HTTP client using device IP and key
    http_client = MerossHttpClient(mc.DEVICE_IP, mc.DEVICE_KEY)

    # Get current state
    response = await http_client.async_request_strict(
        "Appliance.System.All", "GET", {})

    # Check current ON/OFF state setting up command payload accordingly
    is_on = "'onoff': 1,"
    if is_on in str(response):
        payload = {
                    "modeB": [{
                        "channel": 0,
                        "onoff": mc.MTS960_ONOFF_OFF
                    }]
                  }
    else:
        payload = {
                    "modeB": [{
                        "channel": 0,
                        "mode": mc.MTS960_MODE_HEAT_COOL,
                        "working": mc.MTS960_WORKING_HEAT
                    }]
                  }

    # Toggle device ON/OFF
    response = await http_client.async_request_strict(
        "Appliance.Control.Thermostat.ModeB", "SET", payload)

    #print("===========================response=======================")
    #print(response)
    #print("==========================================================")

    # Close aiohttp.ClientSession
    await http_client._session.close()

if __name__ == '__main__':
    asyncio.run(main())