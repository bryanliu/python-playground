import unittest


def bubblesort(arr):
    print("bubble sort before: ", arr)
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    print("bubble sort after: ", arr)
    return arr


def insertsort(arr):
    print("insert sort before: ", arr)
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            tmp = arr[i]
            j = i - 1
            while arr[j] > tmp:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = tmp
    print("insert sort after: ", arr)
    return arr


def selectionsort(arr):
    print("selection sort before: ", arr)
    for i in range(len(arr)):
        min, minidx = float('inf'), 0
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]
    print("selection sort after: ", arr)
    return arr


def partition(arr, i, j) -> int:
    if i > j: return
    pivot = arr[j]
    y = i
    for x in range(i, j):
        if arr[x] < pivot:
            arr[y], arr[x] = arr[x], arr[y]
            y += 1

    arr[y], arr[j] = arr[j], arr[y]
    return y


def quicksortinternal(arr, i, j):
    if i > j: return

    pivot = partition(arr, i, j)
    quicksortinternal(arr, i, pivot - 1)
    quicksortinternal(arr, pivot + 1, j)


def quicksort(arr):
    print("quick sort before: ", arr)

    if not arr: return
    quicksortinternal(arr, 0, len(arr) - 1)

    print("quick sort after: ", arr)
    return arr


class ut(unittest.TestCase):

    def seUp(self):
        pass

    def test_bubble_sort_success(self):
        arr = [3, 4, 5, 6, 7, 2, 1, 33, 3, 6, 8, 9, 2, 1]
        expect = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 33]
        self.assertEqual(expect, bubblesort(arr[:]))

    def test_insert_sort_success(self):
        arr = [3, 4, 5, 6, 7, 2, 1, 33, 3, 6, 8, 9, 2, 1]
        expect = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 33]
        self.assertEqual(expect, insertsort(arr[:]))

    def test_selection_sort_success(self):
        arr = [3, 4, 5, 6, 7, 2, 1, 33, 3, 6, 8, 9, 2, 1]
        expect = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 33]
        self.assertEqual(expect, selectionsort(arr[:]))

    def test_quick_sort_success(self):
        arr = [3, 4, 5, 6, 7, 2, 1, 33, 3, 6, 8, 9, 2, 1]
        expect = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 33]
        self.assertEqual(expect, quicksort(arr[:]))


if __name__ == "__main__":
    unittest.main()
