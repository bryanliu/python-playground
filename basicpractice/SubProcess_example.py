import asyncio
import sys
import locale
"""
这个例子演示了创建一个子进程，然后实施从子进程读输出。
"""
async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    proc = await asyncio.create_subprocess_shell(
        cmd="top",
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    # data = await proc.stdout.readline()
    # line = data.decode('ascii').rstrip()

    # 下面几句可以持续从子进程里面持续读取内容。
    async for line in proc.stdout:
        print("got line:", line)
        #break

    # Wait for the subprocess exit.
    await proc.wait()
    return line

date = asyncio.run(get_date())
print(f"Current date: {date}")