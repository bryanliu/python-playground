input = "/Users/admin/Downloads/demo10.mp4"
outputfile = "/Users/admin/Downloads/demo10_1.mp4"

from ffmpy3 import FFmpeg
import asyncio
import sys
import locale

import time
"""
这个例子想把视频转换写成异步的方式，并且实施更新进度，异步的方式终于是写好了，不过还是不能实施获得输出
在SubProcess_example 中可以实施获得输出，但是这儿同样的方法就是不行，FFmpeg的信息直接就输出出来了。
"""
async def test(i):
    ff = FFmpeg(
        executable="/Users/admin/Downloads/ffmpeg",
        inputs={input: None},
        outputs={outputfile: None}
    )
    print(ff.cmd)
    proc = await ff.run_async(stderr=asyncio.subprocess.PIPE)  # 例子有问题，这句话也要await 才可以运行

    # data = await proc.stdout.readline()
    # line = data.decode('ascii').rstrip()
    # print("read line", line)
    #stdout, stderr = await proc.communicate()
    async for line in proc.stderr:
        print("got line:", line.decode(locale.getpreferredencoding(False)))
    # if stdout:
    #     print(stdout.decode())
    # async for line in proc.stdout:
    #     print(line)
    # while True:
    #     buf = await stderr.read(10)
    #     if not buf:
    #         break

        #print(buf)


    await ff.wait()
    # for j in range(3):
    #     print(i, "run", j)
    #     await asyncio.sleep(1)

# loop = asyncio.get_event_loop()
# task = [test(1)]
# loop.run_until_complete(asyncio.wait(task))
#asyncio.run(test(1))

coroutine1 = test(1)
loop = asyncio.get_event_loop();
task = loop.create_task(coroutine1)
print(task)
loop.run_until_complete(task)
print(task)