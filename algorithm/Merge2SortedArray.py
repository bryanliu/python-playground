import json
import unittest


class Solution(object):
    """
    LC 88. 合并两个有序数组 link: https://leetcode-cn.com/problems/merge-sorted-array/

    给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

    """

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i1, i2, i = m - 1, n - 1, m + n - 1

        while i1 >= 0 and i2 >= 0:
            if nums1[i1] > nums2[i2]:
                nums1[i] = nums1[i1]
                i1 -= 1
            else:
                nums1[i] = nums2[i2]
                i2 -= 1
            i -= 1
        if i1 < 0:
            nums1[:i + 1] = nums2[:i2 + 1]
        return nums1


class Test(unittest.TestCase):

    def test_case(self):
        s = Solution()
        self.assertEqual([2, 5, 6, 0], s.merge([0, 0, 0, 0], 0, [2, 5, 6], 3))


if __name__ == '__main__':
    unittest.main()
