import asyncio
import time
import requests


async def test1(url):
    r = await test2(url)
    print("complete invoike test2", url, r)


async def test2(url):
    r = requests.get(url)
    print("Sent request", url)
    await asyncio.sleep(4)
    print("response", url, time.time() - start)
    return r


url = ["https://segmentfault.com/p/1210000013564725",
       "https://www.jianshu.com/p/83badc8028bd",
       "https://www.baidu.com/"]

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test1(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task))
endtime = time.time() - start
print("Overall time cost: ", endtime)
loop.close()

"""
例子来源 https://www.cnblogs.com/xinghun85/p/9937741.html 
本来三次调用est1, test1 调用test2， 如果是同步的，都应该是顺序执行，test1(url1) test2(url1), test1(url2) test2(url2), test1(url3) test2(url3)
现在可以看到都是并行调用的了。

下面是结果：
Sent request https://segmentfault.com/p/1210000013564725
Sent request https://www.jianshu.com/p/83badc8028bd
Sent request https://www.baidu.com/
response https://segmentfault.com/p/1210000013564725 4.354444980621338
complete invoike test2 https://segmentfault.com/p/1210000013564725 <Response [200]>
response https://www.jianshu.com/p/83badc8028bd 4.572962999343872
complete invoike test2 https://www.jianshu.com/p/83badc8028bd <Response [403]>
response https://www.baidu.com/ 4.6425158977508545
complete invoike test2 https://www.baidu.com/ <Response [200]>
Overall time cost:  4.642789840698242


"""