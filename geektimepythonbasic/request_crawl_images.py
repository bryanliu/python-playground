import re

import requests

content = requests.get("http://www.cnu.cc/discoveryPage/hot-%E4%BA%BA%E5%83%8F")
print(content.text)
pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)  # re.S 点匹配换行符
# 匹配 图集的链接以及Title
# 注意，这边的正则都要用到非贪婪模式，不然就会匹配到最后
subpage = re.findall(pattern, content.text)
# print(results)

for res in subpage:
    # print(res)
    image, name = res
    name = re.sub('\s', '', name)
    # print(image, name)

# 找出所有的<img 标记的图片，并且将jpg 后面的参数去掉。
imgpattern = re.compile(r'<img src="(.*?jpg).*?".*?alt="(.*?)">', re.S)
imgresult = re.findall(imgpattern, content.text)
for res in imgresult:
    print(res)
    # pass
