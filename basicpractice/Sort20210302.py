# coding=utf-8
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:  # 只有 j 和 j+1 的比较，不是j 和 i的比较
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertsort(arr):
    l = len(arr)
    for i in range(1, l):
        if arr[i] < arr[i - 1]:
            tmp = arr[i]
            j = i - 1  # 居然写成了 j = arr[i-1]
            while j >= 0:
                # print( j)
                if arr[j] > tmp:
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
            arr[j + 1] = tmp
    return arr


def selectionsort(arr):
    l = len(arr)
    for i in range(l):
        minval = float('inf')
        minidx = float('inf')
        for j in range(i, l):
            if arr[j] < minval:
                minval = arr[j]
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr


def quicksort(arr):
    def partition(s, e):
        if s == e: return
        pivot = arr[e]

        i = j = s
        while i < e :#写成了 e-1, 已经小于了，写成e 就可以了
            if arr[i] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1

        arr[j], arr[e] = arr[e], arr[j]

        return j

    def sort(s, e):
        if s >= e: return
        pivot = partition(s, e)
        sort(s, pivot - 1)
        sort(pivot + 1, e)

    sort(0, len(arr) - 1)
    return arr


arr = [11, 8, 3, 2, 5, 4, 3, 6, 12]
# print(bubblesort(arr))
# print(insertsort(arr))
# print(selectionsort(arr))
print(quicksort(arr))
