'''

一维数组， 1， 2， 3
没有重复元素, 有重复元素都要考虑，输出其所有子集
[[], [1], [2],[3], [1,2], [2,3], [1,3], [1,2,3]]
'''
import unittest


class Solution:
    def main(self, arr):
        if not arr:
            return []

        res = []

        arr.sort()

        def helper(idx, path):

            nonlocal res

            res.append(path)

            for i in range(idx, len(arr)):
                if i > idx and arr[i] == arr[i - 1]:
                    continue
                helper(i + 1, path + [arr[i]])

        helper(0, [])

        return res


class UT(unittest.TestCase):

    # @unittest.skip
    def testSuccessNoDup(self):
        s = Solution()
        res = s.main([1, 2, 3])
        print(res)
        self.assertEqual([[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], res)

    def testSuccessDup(self):
        s = Solution()
        res = s.main([1, 1, 2, 3])
        print(res)
        self.assertEqual([[], [1], [1, 1], [1, 1, 2], [1, 1, 2, 3], [1, 1, 3], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3],
                          [3]], res)

    # @unittest.skip
    def testEmpty(self):
        s = Solution()
        res = s.main([])
        self.assertEqual([], res)


if __name__ == "__main__":
    unittest.main()
