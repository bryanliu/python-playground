#coding=utf-8
'''
这是一个非原地排序算法，因为产生了额外的数组，原地排序的实现，参考 Sort.py 里面
原理是通过数组元素的交换来达到排序的目的
'''
def quick_sort(list):
    if len(list) == 0:
        return list

    pivot = list[0]

    list1 = [i for i in list[1:] if i > pivot]
    list2 = [i for i in list[1:] if i <=pivot]
    return quick_sort(list1) + [pivot] + quick_sort(list2)

print quick_sort([2,1,3,5,3,7,5,8])