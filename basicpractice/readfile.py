
maxsize = 100

def openfile(path):
    line = 0
    f = open(path)

    readf = f.read
    buf = readf(maxsize)
    while buf:
        line += buf.count("\n")
        buf = readf(maxsize)
    print(line)


openfile("/Users/admin/PycharmProjects/Playground/test")