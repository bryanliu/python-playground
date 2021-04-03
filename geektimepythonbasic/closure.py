"""
用闭包实现一个计数器
"""


def counter(start=0):
    curr = start

    def add_one():
        nonlocal curr
        curr += 1  # 引用外部的 curr
        return curr

    return add_one


count = counter(1)  # 得到一个函数的引用
for _ in range(3):
    print(count())  # 调用这个函数，会依次输出 2，3，4
