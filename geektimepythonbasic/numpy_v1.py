"""
第一次使用 numpy
"""
import numpy as np

# 定义一维矩阵
arr1 = np.array([1, 2])

print(arr1)
print(arr1.dtype)  # int64

# 一维浮点数
arr2 = np.array([1.1, 1.2])
print(arr2)
print(arr2.dtype)  # float64

# 直接和标量计算
print(arr1 * 10)  # 输出 [10, 20], 会对原有数据都乘10

# 多维矩阵
print(np.zeros((3, 4)))  # 3行4列的矩阵，都是0
print(np.ones((2, 5)))  # 2行5列的矩阵，都是1
print(np.empty((3, 5)))  # 3行5列的矩阵，里面的元素是随机值，不是真正的空，空在计算的时候不安全

print(np.arange(10))  # 和 range 类似，输出0到0
print(np.arange(10)[2:4])  # 切片
arr3 = np.arange(10)
arr3[2:4] = 10  # 直接对相应的切片范围内的元素进行赋值
print(arr3)  # >>[ 0  1 10 10  4  5  6  7  8  9]
