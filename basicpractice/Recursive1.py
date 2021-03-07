# -*- coding: UTF-8 -*-


def fact_resursive(i):
    # print i
    if i == 1:
        return 1
    else:
        return i * fact_resursive(i - 1)


def fact_loop(i):
    total = 1
    for y in range(1, i+1):
        total = total * y
    return total


print fact_loop(10000)
# print ("你好")

for i in range(1, 10+1):
    print i