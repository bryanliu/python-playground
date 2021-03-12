import unittest

"""
问题：给定一个整数数组 nums 和一个整数 k，找出 k 个不重叠子数组使得它们的和最大。每个子数组的数字在数组中的位置应该是连续的。返回最大的和。

示例2：

输入: nums = [-1, 4, -2, 3, -2, 3]，k = 2
输出: 8
解释: 4 + (3 + -2 + 3) = 8

这道题目还是蛮难的，主要用了两个备忘录
dp 表示 i个元素，j 组的最优解
m 表示 i 在最后一组里面，j组的最优解
"""


def solution(arr, k):
    n = len(arr)
    dp = [[0] * (k + 1) for _ in range(n + 1)]  # dp[i][j] 表示i个元素分成j组的最大值。
    m = [[0] * (k + 1) for _ in range(n + 1)]  # m[i][j] 表示i一定在第j组里面的最大值

    for i in range(1, len(dp)):
        for j in range(min(i, k), 0, -1):
            # j必须小于等于i，不然就无解了。（有n个元素，最多可以分成n组）
            if i == j:  # 就相当于每个元素自成一组
                m[i][j] = m[i - 1][j - 1] + arr[i - 1]
                dp[i][j] = dp[i - 1][j - 1] + arr[i - 1]
            else:
                m[i][j] = max(m[i - 1][j], dp[i - 1][j - 1]) + arr[i - 1]  # 决策，加到第J组，在J-1组的基础上自成一组
                dp[i][j] = max(dp[i - 1][j], m[i][j])  # 决策，放弃i，或者选择i

    return dp[-1][-1]


class Unittest(unittest.TestCase):

    def test_res(self):
        self.assertEqual(10, solution([1, 2, 3, 4], 1))
        self.assertEqual(8, solution([-1, 4, -2, 3, -2, 3], 2))


if __name__ == "__main__":
    unittest.main()
