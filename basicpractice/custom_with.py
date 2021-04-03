"""
自定义一个类的 with 行为，主要用到 __enter__ 和 __exit__ 两个方法
"""


class Customwith:
    def __enter__(self):

        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):

        if not exc_tb:
            print("finish")
        else:
            print("some error happend", exc_tb)


with Customwith() as a:  # 注意这儿的实例化哦，类 + 括号，而不是写个类名
    # raise (NameError)
    pass
