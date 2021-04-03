from pandas import Series

"""
pandas 是数据预处理和清洗的工具
"""
# 默认索引
obj1 = Series(["a", "b", "c"])
print(obj1)  # 默认索引是 0 开始的数字
"""
0    a
1    b
2    c
dtype: object
"""

# 自定义索引
obj2 = Series(['a', 'b', 'c'], index=['x', 'y', 'z'])
print(obj2)

# 直接用dict 初始化
mp = {1: 'a', 3: 'abc', 5: 'df'}
obj3 = Series(mp)
print(obj3)

# 直接修改索引
obj3.index = [5, 6, 7]
print(obj3)  # 索引变成最新的了。
