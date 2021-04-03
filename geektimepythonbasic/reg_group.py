"""
使用分组功能提取年月日，主要看一下 group 和 groups的区别

"""

import re

r = re.match(r"(\d+)-(\d+)-(\d+)", '2021-04-03')
print(r)
print(r.group(0))  # group(i) 会返回第i个分组
print(r.groups())  # 会以元组的形式返回所有分组
year, month, day = r.groups()
print(year, month, day)  # 输出 2021 04 03
