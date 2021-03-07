#coding=utf-8

def nk(arr,low, high, n):

    if low > high:
        return

    pivot_index = partition(arr, low, high)
    # for example 2,3,4, the biggest one index should be 2
    nbiggestindex = len(arr) - n
    if pivot_index == nbiggestindex:
        return arr[pivot_index]
    if pivot_index < nbiggestindex:
        return nk(arr, pivot_index+1, high, n)
    if pivot_index > nbiggestindex:
        return nk(arr, low, pivot_index - 1, n)


def partition(arr, low, high):

    pivot = arr[high]
    i = j = 0
    while j < high:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        j+=1
    arr[i], arr[j] = arr[j], arr[i]
    return i


arr = [2,4,5, 3]
print(nk(arr, 0, len(arr)-1, 4))