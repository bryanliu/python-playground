import functools
import time

"""
使用装饰器 + 闭包 实现一个显示运行时间的装饰器
"""


def timer(func):
    def wapper(*param):
        start = time.time()
        func(param)
        end = time.time()
        print(f"spend {end - start} to execute the function {func}")

    return wapper


@timer
@functools.lru_cache(None)
def target_func(param):
    print(f"I'm in function with paramaters: {param}")
    time.sleep(1)



# >> spend 1.0040099620819092 to execute the function

if __name__ == "__main__":
    target_func("a", "b")
