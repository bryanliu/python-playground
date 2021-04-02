import os
# This function is built-in function
# Please don't modify it
def SeekFromTail(openedFile, linesToSeek):
    openedFile.seek(0, os.SEEK_END)
    position = openedFile.tell() - 1 
    while position >= 0:
        openedFile.seek(position)
        nextChar = openedFile.read(1)

        if nextChar == "\n":
            position -= 2
            linesToSeek = linesToSeek - 1
            if linesToSeek < 0:
                return position
        else:
            position -= 1

    openedFile.seek(0)

# This function is built-in function
# Please don't modify it 
def ReadLines(openedFile, lineCount):
    if(lineCount > 0):
        result = []
        for i in range(lineCount):
            line = openedFile.readline()
            if(line != ''):
                result.append(line)
        return result
    else:
        return openedFile.readlines()
