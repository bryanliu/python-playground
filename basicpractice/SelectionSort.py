'''
选择排序，时间复杂度 O(n^2)
'''


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        # 加到新的队列，并且从原队列中去掉。
        newArr.append(arr.pop(smallest))

    return newArr

print selectionSort([5,4,6,2])
