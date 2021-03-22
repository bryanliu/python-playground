import unittest


def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


class ut(unittest.TestCase):

    def test_sort_success(self):
        arr = [3, 4, 5, 6, 7, 2, 1, 33, 3, 6, 8, 9, 2, 1]
        expect = [1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 33]

        self.assertEqual(expect, bubblesort(arr[:]))


if __name__ == "__main__":
    unittest.main()
