# coding=utf-8
def bubblesort(arr):

    l = len(arr)
    for i in range(l):
        for j in range(l-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def insertsort(arr):
    l = len(arr)

    for i in range(1, l):
        if arr[i-1] > arr[i]:
            j = i-1
            v = arr[i]
            while j>=0:
                if arr[j] > v:
                    arr[j+1] = arr[j]
                    j -= 1 #忘了 - 1 了
                else:
                    break #忘了Break了
            arr[j+1] = v
    return arr

def selectionsort(arr):
    for i in range(len(arr)):
        minv = arr[i]
        minidx = i
        for j in range(i, len(arr)):
            if arr[j]< minv:
                minv = arr[j] #忘了对 minv重新赋值了。
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]

    return arr

def partition(x, y, arr):
    pivot = arr[y]
    i, j = x, x #这边 j 居然写成 y-1.  结果肯定错了。
    while j < y: #因为上面的错误，这边也写成了 i < j 了
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[y] = arr[y], arr[i]
    return i

def quicksort(i, j, arr):

    if i > j: return
    idx = partition(i, j, arr)
    quicksort(i, idx-1, arr)
    quicksort(idx+1,j, arr)

    return arr

arr = [11,8,3,2,5,4,3,6,12]
#print(bubblesort(arr))
#print(insertsort(arr))
#print(selectionsort(arr))
print(quicksort(0, len(arr)-1, arr))