# coding=utf-8

def bubbleSort(arr):

    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def insertSort2(arr):
    n = len(arr)

    for i in range(1, n):
        value = arr[i]
        j = i-1
        while j >=0:
            if arr[j] > value:
                arr[j+1] = arr[j]
            else:
                break
            j-=1
        arr[j+1] = value

    return arr
# 二刷，错了好多，while j >0 不是 arr[j] > value,  arr[j+1] = value 不是 arr[j] = value

def insertSort3(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            j = i-1
            v = arr[i]
            while j >= 0: #这边判断边界就可以
                if arr[j] > v:
                    arr[j+1] = arr[j]
                else:
                    break
                j -= 1
            arr[j+1] = v

    return arr

def insertSort(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            v = arr[i]
            j = i-1
            while j >= 0:
                if arr[j] > v:
                    arr[j+1] = arr[j]
                    j -= 1
                else:
                    break
            arr[j+1] = v

    return arr



def selectionSort2(arr):

    n = len(arr)
    for i in range(n):
        min_value = float("inf")
        min_index = -1
        for j in range(i, n):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def selectionSort(arr):
    for i in range(len(arr)):

        min, minidx = arr[i], i
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

# 二刷，把min_value 的声明放到 j 循环里面了


def mergeSort(arr):

    if len(arr) <=0:
        return

    if len(arr) == 1:
        return arr


    middle = len(arr)//2

    arr = merge(mergeSort(arr[:middle]), mergeSort(arr[middle:]))
    return arr

def merge(arr1, arr2):

    newArr = []

    i = j = 0
    while i < len(arr1) and j < len(arr2) :
        if arr1[i] < arr2[j]:
            newArr.append(arr1[i])
            i+=1
        else:
            newArr.append(arr2[j])
            j+=1

    if i < len(arr1):
        newArr = newArr + arr1[i:]
    if j < len(arr2):
        newArr = newArr + arr2[j:]
    return newArr
'''
丢数据，这段代码丢了三个数据，一个是数组的下表，尾下标是不包括的
i < len(arr) 而不是 i< len(arr)-1 少了一个数据
newArr = newArr + arr1， 一定要赋值回去
'''



def partition2(arr, low, high):

    pivot = arr[high]
    i=j=low
    while j < high:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        j+=1
    arr[i], arr[high] = arr[high], arr[i]
    print(i+1)
    print(arr[i])
    return i

def quickSort3(arr, low, high):
    if low > high:
        return
    pivot_index = partition2(arr, low, high)
    quickSort3(arr, low, pivot_index-1)
    quickSort3(arr, pivot_index+1, high)
    #这儿出错了，递归应该把 pivot 去掉，所以 要 -1, 下面一个 +1

    return arr

def partition3(arr, low, high):
    pivot = arr[high]
    i = j = low
    while j < high:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort2(arr, low, high):
    if low > high: return
    idx = partition3(arr, low, high)
    quickSort2(arr, low, idx - 1)
    quickSort2(arr, idx + 1, high)
    return arr


arr = [11,8,3,2,5,4,3,6,12]
#print bubbleSort(arr)
#print insertSort(arr)
#print selectionSort(arr)
#print(mergeSort(arr))
print (quickSort2(arr, 0, len(arr)-1))