from pandas import Series, DataFrame

"""
pandas 是数据预处理和清洗的工具
"""
# # 默认索引
# obj1 = Series(["a", "b", "c"])
# print(obj1)  # 默认索引是 0 开始的数字
# """
# 0    a
# 1    b
# 2    c
# dtype: object
# """
#
# # 自定义索引
# obj2 = Series(['a', 'b', 'c'], index=['x', 'y', 'z'])
# print(obj2)
#
# # 直接用dict 初始化
# mp = {1: 'a', 3: 'abc', 5: 'df'}
# obj3 = Series(mp)
# print(obj3)
#
# # 直接修改索引
# obj3.index = [5, 6, 7]
# print(obj3)  # 索引变成最新的了。

# 重新索引，并且增加索引，默认新增索引对应的值是NAN，可以设置默认值
# ser1 = Series(["q", "b", "c"], index=[1, 2, 3])
# print(ser1)
# """
# 1    q
# 2    b
# 3    c
# """
# ser2 = ser1.reindex([3, 2, 1, 0])
# print(ser2)
# """ 其实可以看到就是把顺序重新安排一下，如果有个新的索引，默认插入一个Nan
# 3      c
# 2      b
# 1      q
# 0    NaN
# """
# # 删掉缺失值
# print(ser2.dropna())

# 设置默认值
# ser3 = ser1.reindex([3, 2, 1, 0], fill_value=-1)
# print(ser3)
# """
# 3     c
# 2     b
# 1     q
# 0    -1
# """
# ser4 = ser1.reindex([3,2,1,0], method='bfill')
# print(ser4)
# """
# 用相邻的后面一个值填充 method='bfill', ffill用前面的一个值填充
# 3    c
# 2    b
# 1    q
# 0    q
# """



# data = {"city": ["shanghai", "suzhou", "changzhou", "wuxi"],
#         "year": [1998, 2002, 2001, 2021],
#         "month": [2, 6, 3, 1]}
#
# df1 = DataFrame(data)
# print(df1)
# """
#         city  year  month
# 0   shanghai  1998      2
# 1     suzhou  2002      6
# 2  changzhou  2001      3
# 3       wuxi  2021      1
# """
#
# # 调整column 顺序
# df2 = DataFrame(data, columns=["year", "month", "city"])
# # df2.sort_values(by="year")
# # df2.sort_index(axis=0)
# print(df2)
#
# # 取得单列值，下面两种方式是一样的
# print(df2["city"])
# print(df2.city)
#
# # 增加一列
# df2["new"] = 100  # 增加一个新的列，每行的值都是100
# print(df2)
# """
# Name: city, dtype: object
#    year  month       city  new
# 0  1998      2   shanghai  100
# 1  2002      6     suzhou  100
# 2  2001      3  changzhou  100
# 3  2021      1       wuxi  100
# """
#
# # 增加一列，由其他列计算而来
# df2['monthdouble'] = df2.month * 2
# print(df2)
# """
#    year  month       city  new  monthdouble
# 0  1998      2   shanghai  100            4
# 1  2002      6     suzhou  100           12
# 2  2001      3  changzhou  100            6
# 3  2021      1       wuxi  100            2
# """
# #行列互换
# print(df2.T)
#
# from numpy import nan as na
# df3 = DataFrame([[1., 2, na], [2., na, na], [na, na, na]])
# print(df3)
# """
#      0    1   2
# 0  1.0  2.0 NaN
# 1  2.0  NaN NaN
# 2  NaN  NaN NaN
# """
#
# # 删除全部NA, 只要一行里面有NA，这行就会被整个删掉。
# print(df3.dropna())
# # 没了，全部被清空了
#
# # 只有整行全部是NA才能被删掉
# print(df3.dropna(how='all'))
# """
#      0    1   2
# 0  1.0  2.0 NaN
# 1  2.0  NaN NaN
# """
#
# # 只有整列全部是NA才删掉
# print(df3.dropna(axis=1, how='all'))
# """
#      0    1
# 0  1.0  2.0
# 1  2.0  NaN
# 2  NaN  NaN
# """
#
# # 填充空值
# print(df3.fillna(0))
# """
#      0    1    2
# 0  1.0  2.0  0.0
# 1  2.0  0.0  0.0
# 2  0.0  0.0  0.0
# """
# # 在原有 dataframe上填充，
# df3.fillna(0, inplace=True)
# print(df3) # 和上面一样，不过这次修改了自身

# 多层索引
ser5 = Series(['va', 'vb', 'vc'], index=[['a', 'a', 'b'], ['1', '2', '1']])
print(ser5)
"""
a  1    va
   2    vb
b  1    vc
"""
print(ser5['a']) # 可以取出 索引a的全部数据
"""
1    va
2    vb
"""
print(ser5['a':'b']) # 支持多个索引
"""
a  1    va
   2    vb
b  1    vc
"""
# series 转 dataframe
print(ser5.unstack())
"""
    1    2
a  va   vb
b  vc  NaN
"""
# dataframe 转为 series
print(ser5.unstack().stack()) # 结果和之前一样
