import unittest


def lsc(s1, s2):
    h, w = len(s1) + 1, len(s2) + 1  # 加个哨兵，方便处理
    dp = [[0] * w for _ in range(h)]

    for i in range(1, h):
        for j in range(1, w):

            if s1[i - 1] == s2[j - 1]:  # i 和 j 又反了
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


class TestCase(unittest.TestCase):

    def test_lsc(self):
        self.assertEqual(3, lsc("abcde", "ade"))
        self.assertEqual(3, lsc("fosh", "fish"))
        self.assertEqual(5, lsc("helloworld", "hollachild"))
        self.assertEqual(4, lsc("mtacnu", "mitcmu"))
