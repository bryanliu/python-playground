def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertsort(arr):
    for i in range(1, len(arr)):
        j = i-1
        v = arr[i]
        while j >=0:
            if arr[j] > v:
                arr[j + 1] = arr[j]
            else:
                break
            j -= 1
        arr[j + 1] = v
    return arr


def insersort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i-1
        while j >=0:
            if arr[j] >tmp:
                arr[j+1] = arr[j]
                j -= 1
            else:
                break

        arr[j+1] = tmp
    return arr


def selectionsort(arr):
    for i in range(len(arr)):
        min_v = float('inf')
        min_idx = -1
        for j in range(i, len(arr)):
            #min_v, min_idx = float('inf'), -1

            if arr[j] < min_v:
                min_v = arr[j]
                min_idx = j
        #print(i, min_idx)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def mergesort(arr):
    if not arr: return
    if len(arr) == 1: return arr
    mid = len(arr) // 2
    return merge(mergesort(arr[:mid]), mergesort(arr[mid:]))

def merge(arr1, arr2):
    newarr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            newarr.append(arr1[i])
            i += 1
        else:
            newarr.append(arr2[j])
            j += 1
    if i < len(arr1):
        newarr += arr1[i:]
    if j < len(arr2):
        newarr += arr2[j:]
    return newarr



def quicksort(arr):
    def qsort(l, r):
        if l ==r:
            return
        mid = patition(l, r)
        qsort(l, mid - 1)
        qsort(mid + 1, r)

    def patition(l, r):

        pivot = arr[r]
        j = 0
        for i in range(l, r):
            if arr[i] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[j], arr[r] = arr[r], arr[j]
        return j
    qsort(0, len(arr) - 1)
    return arr

arr = [1,3,2,5,4]
print bubblesort(arr[:])
print insersort(arr[:])
print selectionsort(arr[:])
print mergesort(arr[:])
print quicksort(arr[:])
