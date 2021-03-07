
try:
    #raise IOError, "hahaha"
    file=open('test', 'a')
    for i in range(1):
        file.write("only for test"+str(i)+"\n")
except IOError, e:
    print 1, "error ", e
else:
    print 'success'
finally:
   print 'finally'

