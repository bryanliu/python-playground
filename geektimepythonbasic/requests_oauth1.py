import requests
from requests_oauthlib import OAuth1

'''
使用OAuth的认证方式调用 TS 的API
'''

url = "https://api-sandbox.tradeshiftchina.cn/tradeshift/rest/external/cn-pay-ultimate-fapiao-lookup/mock/invoice"
data = {"invoiceNumber": "25073946"}
auth = OAuth1(client_key="OwnAccount", client_secret="OwnAccount",
              resource_owner_key="a3nm8sw7Jc6gF6q7Wm-G2GR+-K9SbG",
              resource_owner_secret="8TJSakwtgb6Chyy65GWG8HuJCCK7vcV+uJ4xJw4e")

resp = requests.get(url, auth=auth, params=data)
print(resp.json())
