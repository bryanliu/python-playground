# coding=utf-8

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertsort(arr):
    for i in range(1, len(arr)):
        j = i-1
        value = arr[i]
        while j >= 0:
            if arr[j] > value:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        arr[j+1] = value
    return arr

def selectionsort(arr):
    for i in range(len(arr)):
        minv = float('inf')
        minindex = -1
        for j in range(i, len(arr)):
            if arr[j] < minv:
                minv = arr[j]
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

def mergesort(arr):
    def merge(arr1, arr2):
        result = []
        i = j = 0
        while i<len(arr1) and j<len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        if i < len(arr1) :
            result += arr1[i:]
        if j < len(arr2) :
            result += arr2[j:]
        return result


    def sort(arr):
        if len(arr) <=1:
            return arr
        mid = len(arr)/2
        return merge(sort(arr[:mid]), sort(arr[mid:]))

    return sort(arr)

def quicksort_inplace(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = j = low
        while j < high:
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
            j += 1
        arr[i], arr[j] = arr[j], arr[i]
        return i

    def sort(arr, low, high):
        if low >= high: return
        mid = partition(arr, low, high)
        sort(arr, low, mid - 1)
        sort(arr, mid + 1, high)
        pass

    sort(arr, 0, len(arr)-1) #
    return arr


arr = [11,8,3,2,5,4,3,6,12]
#print bubblesort(arr)
#print insertsort(arr)
#print selectionsort(arr)
#print mergesort(arr)
print quicksort_inplace(arr)


