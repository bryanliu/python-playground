# input = "/Users/admin/Downloads/landing_moscow_airport.mp4"
# outputfile = "/Users/admin/Downloads/demo18.mp4"

import os
import time

from ffmpy3 import FFmpeg

ffmpgeexecutable = "/Users/admin/Downloads/ffmpeg"


def convertvideos(input, output=None):
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
            outputpath = os.path.join(output, file)
            print(inputpath)
            print(outputpath)
            convert(inputpath, outputpath)


def convert(input, output):
    ff = FFmpeg(executable=ffmpgeexecutable,
                inputs={input: None},
                # outputs={outputfile: '-vn -ar 44100 -ac 2 -ab 192 -f wav'}
                # outputs={outputfile: '-vf fps=fps=10 -vf scale=iw/2:ih/2 '}
                # outputs={outputfile: ' -r 30 -vf scale=iw/2:ih/2'}
                outputs={output: '-b:v 1500k'}

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
    convertvideos("/Users/admin/Downloads/test")
