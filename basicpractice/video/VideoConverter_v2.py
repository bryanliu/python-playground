input = "/Users/admin/Downloads/demo10.mp4"
output = "/Users/admin/Downloads/demo10_1.mp4"

import ffmpeg
import locale

process = (
    ffmpeg
        .input(input)
        .output(output)
        # .run(quiet=True, overwrite_output=True)
        .run_async(pipe_stdout=True, pipe_stderr=True)
)

#ut, err = process.communicate()
#print(out)

for line in process.stderr:
    print("got line:", line.decode(locale.getpreferredencoding(False)))