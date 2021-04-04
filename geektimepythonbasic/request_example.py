import requests

data = {"user": "1", "name": "whoami"}
resp = requests.get("http://httpbin.org/get", data=data)
print(resp.text)

resp = requests.post("http://httpbin.org/post", data=data)
print(resp.json())  # 可以转成其他格式，比如json
