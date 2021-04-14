import base64
import datetime
import hashlib
import hmac
import json

import requests

import time

base_url = "https://api.sandbox.gemini.com"

gemini_api_key = "account-zmidXEwP72yLSSybXVvn"
gemini_api_secret = "375b97HfE7E4tL8YaP3SJ239Pky9".encode()

t = datetime.datetime.now()
payload_nonce = str(int(time.mktime(t.timetuple()) * 1000))

# endpoint = "/v1/order/new"
# url = base_url + endpoint
# payload = {
#     "request": "/v1/order/new",
#     "nonce": payload_nonce,
#     "symbol": "btcusd",
#     "amount": "1",
#     "price": "3633443.00",
#     "side": "buy",
#     "type": "exchange limit",
#     "options": ["maker-or-cancel"]
# }

endpoint = "/v1/mytrades"
url = base_url + endpoint

payload = {
    "nonce": payload_nonce,
    "request": "/v1/mytrades",
    "symbol": "btcusd"
}

encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()

request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
}

response = requests.post(url,
                         data=None,
                         headers=request_headers)

new_order = response.json()
print(json.dumps(new_order, indent=4))

########## 输出 ##########
