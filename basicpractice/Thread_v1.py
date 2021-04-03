"""
实现一个多线程的例子
"""
import threading
from threading import current_thread


def dosth(a):
    print("current thread", current_thread().getName(), "start")
    print("i'm doing something", str(a))
    print("current thread", current_thread().getName(), "stop")


for i in range(10):
    t = threading.Thread(target=dosth, args=[i])  # target 方法名，args 参数列表，用list传进去，即使只有一个
    t.start()
    t.join()  # 和主线程Join起来，让主线程等待

print("main thread stop")
