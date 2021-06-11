import timeit
'''
这个测试用来测试 for in range(len(arr)) 和 for in arr 的性能
发现前者花费的时间是后者的3倍
'''

arr = [i for i in range(100000)]

def for_range():
    for i in range(len(arr)):
        pass

def for_arr():
    for i in arr:
        pass

print("for in range(len)", timeit.timeit(stmt='for_range()', setup="from __main__ import for_range", number=1000))
print("for in array", timeit.timeit(stmt='for_arr()', setup="from __main__ import for_arr", number=1000))

'''
for in range(len) 2.308525469
for in array 0.808130942
'''