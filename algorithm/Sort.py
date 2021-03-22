import unittest


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr

def insertsort(arr):
    print("insert sort before: ", arr)
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            tmp = arr[i]
            j = i-1
            while arr[j] > tmp:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = tmp
    print("insert sort after: ", arr)
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


if __name__ == "__main__":
    unittest.main()
