"""
static constants symbols for Meross protocol symbols/semantics
"""

# ===================================================
# Meross device LAN IP
DEVICE_IP = "192.168.XXX.XXX"
# Meross device key, 32 character alphanumeric string,
# e.g 2a1278l78784dbiv8i1y1weuhrikz9mh
DEVICE_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# ===================================================


# misc keys for json payloads
KEY_HEADER = "header"
KEY_MESSAGEID = "messageId"
KEY_NAMESPACE = "namespace"
KEY_METHOD = "method"
KEY_PAYLOADVERSION = "payloadVersion"
KEY_FROM = "from"
KEY_PAYLOAD = "payload"
KEY_TIMESTAMP = "timestamp"
KEY_TIMESTAMPMS = "timestampMs"
KEY_SIGN = "sign"
KEY_CODE = "code"
KEY_NONCE = 'nonce'
KEY_PARAMS = 'params'
KEY_APISTATUS = 'apiStatus'
KEY_TOKEN = 'token'
KEY_INFO = 'info'
KEY_DATA = 'data'
KEY_KEY = 'key'

# Meross cloud HTTP api
MEROSS_API_V1_URL = 'https://iot.meross.com/v1'
MEROSS_API_SIGNIN_PATH = '/Auth/signIn'
MEROSS_API_LOGOUT_PATH = '/Profile/Logout'

# Errors
METHOD_ERROR = "ERROR"
KEY_ERROR = "error"
# error codes as reported by Meross device protocol
ERROR_INVALIDKEY = 5001

# GP constants
MANUFACTURER = "Meross"

# Meross mts960 smart socket thermostat specific values:
# 1°C = x100 device value
MTS960_TEMP_SCALE = 100 
# device modes
MTS960_MODE_HEAT_COOL = 1
MTS960_MODE_SCHEDULE = 2
MTS960_MODE_TIMER = 3
# socket state
MTS960_STATE_UNKNOWN = 0
MTS960_STATE_ON_ON = 1 # thermostat ON, socket ON
MTS960_STATE_ON_OFF = 2  # thermostat ON, socket OFF
MTS960_STATE_OFF_OFF = 3  # thermostat OFF, socket OFF
# working mode
MTS960_WORKING_HEAT = 1
MTS960_WORKING_COOL = 2
# device power ON/OFF
MTS960_ONOFF_ON = 1  # thermostat ON
MTS960_ONOFF_OFF = 2  # thermostat OFF
# device timer mode type
MTS960_TIMER_TYPE_COUNTDOWN = 1
MTS960_TIMER_TYPE_CYCLE = 2
