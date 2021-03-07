# coding=utf-8
# Using resursive to sum the list
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

# print sum([1,2,3,4,6])

# Using recursive to calculate the count
def listCount(list):
    if not list:
        return 0
    else:
        return 1 + listCount(list[1:])

# print listCount([1,1,1,1,11,11,1,1,1,1,1,])

# Using recursive to find the max value in list
def findMaxNumber(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = findMaxNumber(list[1:])
    return sub_max if sub_max > list[0] else list[0]

#print findMaxNumber([2, 3, 4, 5, 6, 4, 1, 3, 4, 5, 6, 7, 8, 23, 12])

def binary_search(list, guess):
    if len(list) == 1:
        if list[0] == guess:
            return 'bingo'
        return None

    mid_index = len(list)/2
    mid_value = list[mid_index]
    if mid_value > guess:
        # 注意：截取子字符串的时候，尾下标的是不包含的，所以不能减一
        return binary_search(list[:mid_index], guess)
    else:
        return binary_search(list[mid_index:], guess)

print binary_search([1,2,3], 4)

