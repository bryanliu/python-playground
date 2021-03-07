# coding=utf-8

nums = [2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,1,3,1,3,1,3,1,3,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2]

def partition2(begin, end):
    left, right = begin, end
    while left < right:
        while left < right and nums[left] < nums[right]:
            right -= 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        while left < right and nums[left] < nums[right]:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
    return left


def partition(i, j):
    pivot = nums[j]

    x = y = i  # 为啥写成 x, y = i
    while y < j:
        if nums[y] <= pivot:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
        y += 1
    nums[x], nums[j] = nums[j], nums[x]
    return x


i, j = 0, len(nums) - 1
mid = (i + j) // 2
print(mid)
median = 0
while True:
    print("check median start: ", "mid", mid, "i", i, "j", j, "             initial", nums[i: j + 1])
    x = partition2(i, j)
    print("check median result:", "mid", mid, "i", i, "j", j, "result", x, "result", nums[i: j + 1])
    #print(nums[i: j + 1])
    if x < mid:
        i = x + 1
    elif x > mid:
        j = x - 1
    else:
        median = nums[x]
        break
# 3 way partitation
print(median)