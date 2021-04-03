"""
yield 实现迭代器的例子，简单点理解，定义的函数作为一个迭代器，到yield的地方会停下来。
"""


def frange(start=0.0, end=0.0, step=1.0):
    x = start
    while x < end:
        yield x  # 走到这儿就停了，同时会记录x的值
        x += step


for i in frange(3.2, 4.9, 0.002):
    print(i)
