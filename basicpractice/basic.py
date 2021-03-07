#raw_input('please input something: ')
import calendar
import time
from math import floor, pi
from random import random, uniform

a = b = c= 1
d, e, f = 1, 2.2, 'san'
g = 3e+26j

print (a,b ,c ,d, e, f, repr(g))
print f[0:] * 40


dict = {}
dict["ha"] = "hei"
dict[2] = 2.0

print dict
print dict.keys()
print dict.values()

dict2 = {"a" : 1, "john" : 'hahahaha' }
print dict2
print dict2.keys()
print dict2.values()

print 1/2
print 1/float(2)
print "a" * 10
print 10//3
print 10 % 3
print 2 ** 10
a = 00111100
print a<<2

print int(random()*100)
print int(uniform(1, 13))

for i in range(10):
    print uniform(1, i),

else:
    print "loop finished"

print "hello world".zfill(100)
print "hello".center(50)
print "hello".title()

list1 = [i for i in range(10)]
print list1

list2 = [[uniform(0, i) for i in range(5)] for i in range(3)]
print list2

cal = calendar.month(2019, 9)
print cal
print time.clock()
print time.time()
time.sleep(1)
print time.clock()
print time.time()