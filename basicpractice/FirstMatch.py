# coding=utf-8

def firstMatch(arr, a):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + ((high - low) >> 1)
        midvalue = arr[mid]
        if midvalue < a:
            low = mid + 1
        elif midvalue > a:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != a:
                return mid
            else:
                high = mid - 1


def lastMatch(arr, a):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)

        if arr[mid] < a:
            low = mid + 1
        elif arr[mid] > a:
            high = mid - 1
        else:
            if mid == len(arr) - 1 or arr[mid + 1] > a:
                return mid
            else:
                low = mid + 1
'''
数组是用 [] 引用的，不是()
'''

def firstBigger(arr, a):

    low, high = 0, len(arr) - 1
    while low <= high:

        mid = low + ((high - low) >> 1)
        if arr[mid] <= a:
            low = mid + 1
        else:
            if mid == 0 or arr[mid-1] <= a:
                return mid
            else:
                high = mid -1

def lastLess(arr, a):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) >> 1)
        if (arr[mid] >= a):
            high = mid -1
        else:
            if arr[mid] == len(arr) or arr[mid + 1] >= a:
                return mid
            else: low = mid +1



arr1 = [1, 3, 4, 5, 6, 8, 8, 8, 11, 18]
print lastLess(arr1, 6)
