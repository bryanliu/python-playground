"""
实现一个多线程的例子
"""
import threading
from threading import current_thread

#
# def dosth(a):
#     print("current thread", current_thread().getName(), "start")
#     print("i'm doing something", str(a))
#     print("current thread", current_thread().getName(), "stop")
#
#
# for i in range(10):
#     t = threading.Thread(target=dosth, args=[i])  # target 方法名，args 参数列表，用list传进去，即使只有一个
#     t.start()
#     t.join()  # 和主线程Join起来，让主线程等待
#
# print("main thread stop")

"""
实现一个多线程的例子 2
"""


class Mythread(threading.Thread):
    def run(self) -> None:
        print("run thread", current_thread().getName(), "start")
        print("run")
        print("run thread", current_thread().getName(), "stop")


for _ in range(10):
    t1 = Mythread()
    t1.start()
    # t1.join() #如果不加这个，那主线程就极有可能比其他线程先执行完

print('main thread stop', current_thread().getName())
