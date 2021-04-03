"""
这个例子用queue 来实现一个生产者，消费者模式
生产者和消费者都是多线程的。
同时练习了 time, threading, random, queue 的使用
"""
import random
import threading
import time
from queue import Queue
from threading import current_thread

queue = Queue(20)


class Producer(threading.Thread):
    def run(self) -> None:
        """
        随机生成一个数字，塞到队列中，然后随机睡会儿。
        :return:
        """
        global queue
        nums = range(100)
        while True:
            v = random.choice(nums)
            queue.put(v)
            print("Producer %s put to queue, value is: %s" % (current_thread().getName(), v))
            time.sleep(random.randint(1, 3))


class Consumer(threading.Thread):
    def run(self):
        """
        从队列中获取元素，然后随机睡会儿
        :return:
        """
        global queue
        while True:
            v = queue.get()
            queue.task_done()
            print("Consumer %s got the value: %s" % (current_thread().getName(), v))
            time.sleep(random.randint(1, 5))


# 初始化一些生产者
Producer().start()
Producer().start()
Producer().start()
Producer().start()
Producer().start()

# 初始化一些消费者
Consumer().start()
Consumer().start()
# Consumer().start()
# Consumer().start()
# Consumer().start()
# Consumer().start()
# Consumer().start()
# Consumer().start()
# Consumer().start()
