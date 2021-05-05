# input = "/Users/admin/Downloads/landing_moscow_airport.mp4"
# outputfile = "/Users/admin/Downloads/demo18.mp4"

import os
import subprocess
import time

from ffmpy3 import FFmpeg
from configparser import ConfigParser

ffmpgeexecutable = r""
input = ""
def init():
    curr = os.path.abspath(".")
    print("current folder: ", curr)
    global ffmpgeexecutable, input
    configpath = os.path.abspath(r".env")
    conn = ConfigParser()
    conn.read(configpath)
    ffmpgeexecutable = conn.get('config', 'ffmpeg_executable')
    input = conn.get('config', 'input')

def convertvideos(output=None):

    init()

    if not os.path.exists(input):
        print("input path not exists, please verify!")
        return

    if not output or not os.path.exists(output):
        print("output folder not exists, using input/result as default folder")
        output = os.path.join(input, "result")
        if not os.path.exists(output):
            os.makedirs(output)

    filenames = os.listdir(input)

    for file in filenames:
        inputpath = os.path.join(input, file)
        if os.path.isfile(inputpath) and file.split(".")[-1].lower() in ['mp4', 'mkv', 'avi']:
            filename = file.split(".")[0]
            # all convert to mp4
            outputpath = os.path.join(output, filename + ".mp4")
            print(inputpath)
            print(outputpath)
            convert(inputpath, outputpath)

            # Rename
            newname = os.path.join(output, filename)
            os.rename(outputpath, newname)


def convert(input, output):
    ff = FFmpeg(executable=ffmpgeexecutable,
                inputs={input: None},

                # outputs={output: '-vn -ar 44100 -ac 2 -ab 192 -f wav'}
                # outputs={output: '-vf fps=fps=10 -vf scale=iw/2:ih/2 '}
                # outputs={output: ' -r 30 -vf scale=iw/2:ih/2'}
                # outputs={output: '-b:v 2500k -vf scale=iw*0.7:ih*0.7'} #分辨率变为原来的70%
                # outputs={output: '-b:v 2500k'} #码率
                outputs={output: ''}  # avi 到 mp4 只是编码转一下，就可以缩小一半的体积，原来码率差不多要5M，现在之哟啊2.2M左右

                )
    print(ff.cmd)
    start = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
    ff.run()
    # ff.run_async()
    # await ff.wait()
    end = time.time()

    print(f"spend {end - start} to complete the task")


if __name__ == "__main__":
    # convert()
    convertvideos()
