# -*- coding: UTF-8 -*-
'''
最长子串之和，给定一个数组, 找出连续的数组之和是最大的。

结题要点：只要是正的就可以一直往后累加
如果累加结果是负的，果断丢弃，因为如果往后累加，只会减少累加的结果

'''
def max_sub_total(arr):
    '''
    一次循环就搞定最大值，
    :param arr:
    :return:
    '''
    max = 0
    total = 0
    for i in arr:
        total += i
        if max < total:
            max = total
        if total <= 0:
            total = 0
    return max


print  max_sub_total([-2, 11, -4, 13, -5, -20, 20, 25])
