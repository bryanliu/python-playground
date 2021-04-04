import re

import requests

content = requests.get("http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F")
print(content.text)
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)  # re.S 点匹配换行符
# 匹配 图集的链接以及Title
# 注意，这边的正则都要用到非贪婪模式，不然就会匹配到最后
results = re.findall(pattern, content.text)
# print(results)

for res in results:
    # print(res)
    image, name = res
    name = re.sub('\s', '', name)
    print(image, name)
