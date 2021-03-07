# coding=utf-8

import heapq
def bubblesort(arr):

    for i in range(len(arr)):
        for j in range(1, len(arr)-i): #错误，每次都是从1开始啊，不是从i开始 i只是用来计数和 限制 j 的 尾标
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
        print arr
    print arr

def insertsort(arr):

    for i in range(1,len(arr)):
        value = arr[i]
        j = i-1
        while j >=0:
            if arr[j] > value: # 和 value 比，不是和 arr[i] 比，
                arr[j+1] = arr[j]
                j-=1
            else:
                break
        arr[j+1] = value
    print arr

def selectionsort(arr):

    for i in range(0, len(arr)):
        minvalue = float("inf")
        minindex = -1
        for j in range(i, len(arr)):# 应该从i开始而不是 i+1开始
            if arr[j] < minvalue:
                minvalue = arr[j]
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
        print i, arr
    print arr

def mergesort(arr):
    def msort(arr):
        if len(arr) ==1:
            return arr
        mid = len(arr)/2
        return merge(msort(arr[:mid]), msort(arr[mid:]))

    def merge(arr1, arr2):
        arr = []
        i = j = 0
        while i< len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i+=1
            else:
                arr.append(arr2[j])
                j+=1
        if i < len(arr1): # 这边是 i < len(arr1) 不是 < len(arr1) +1 因为正常走完，i = len(arr) 的，因为每次都要 i + 1
            arr += arr1[i:]
        if j < len(arr2):
            arr += arr2[j:]
        return arr

    print msort(arr)

def qsort1(arr):
    '''
    with extra space b/c generate the new array
    :param arr:
    :return:
    '''
    if len(arr) <= 1: return arr
    pivot = arr[0]

    return qsort1([i for i in arr[1:] if i<pivot]) + [pivot] + qsort1([i for i in arr[1:] if i>=pivot])
    '''
    几个问题：中间的pivot 没有拿中括号括起来
    取小于pivot的时候，没有 去掉 pivot那个元素，应该这么写 arr[1:]
    '''

def qsort2(arr):
    '''
    原地分区，都要原地排序，不能产生额外空间
    :param arr:
    :return:
    '''
    def qsort(arr,low, high):
        if low > high: return
        index = partition(arr, low, high)
        qsort(arr, low, index-1)
        qsort(arr, index+1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = j = low
        while j <high:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1

        arr[i], arr[j] = arr[j], arr[i]
        return i

    qsort(arr, 0, len(arr)-1) # high 传进去是 len(arr) - 1s
    print arr

def heapsort(arr):

    heap = []
    result = []

    for i in arr:
        heapq.heappush(heap, -i)

    while heap:
        result.append(-heapq.heappop(heap))
    return result



arr = [11,8,3,2,5,4,3,6,12]
#bubblesort(arr)
#insertsort(arr)
#selectionsort(arr)
#mergesort(arr)
#print qsort1(arr)
#qsort2(arr)
print heapsort(arr)




