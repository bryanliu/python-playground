from urllib import parse
from urllib import request

# get 方式
resp = request.urlopen("http://httpbin.org/get", timeout=1)
print(resp.read().decode('utf-8'))  # 需要decode 并制定字符集，不然中文会解码失败

# post
# 注意这儿一定要用bytes包一下，而且要指定encoding
data = bytes(parse.urlencode({"hello": "world"}), encoding='utf-8')
resp = request.urlopen("http://httpbin.org/post", data=data)
print(resp.read().decode('utf-8'))

# 自定义header
headers = {
    "User-Agent": "top browser"
}
# 注意这边先构建一个Request对象，把Header传进去
data = bytes(parse.urlencode({"hello": "world"}), encoding='utf-8')
req = request.Request(url="http://httpbin.org/post", headers=headers, data=data, method="POST")
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))
