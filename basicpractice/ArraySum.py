def sum_loop(arr):
    total = 0
    for i in arr:
        total = total + i
    return total


def sum_recursion(arr):

    if len(arr) == 0:
        return 0  # Base case
    else:
        return arr[0] + sum_recursion(arr[1:])  # Recursive case


arr = [2, 3, 4, 4, 5, 7, 8, 9, 0, 0, 2, 3, 45, 78, 28, 39]
print sum_recursion(arr)
print sum_loop(arr)



