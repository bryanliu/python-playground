"""
如果装饰器本身有参数的话，我们需要再套一层闭包
"""

def tip(args):
    def tip_internal(func):
        def wrapper(a, b):
            print("current doing", args)
            func(a, b)
        return wrapper
    return tip_internal

@tip("add")
def add(a, b):
    print(a + b)

@tip("sub")
def sub(a, b):
    print(a-b)

add(1, 2)
#>>current doing add
#>> 3
sub(2, 1)
#>>current doing sub
#>> 1