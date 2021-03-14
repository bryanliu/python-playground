import unittest
from typing import List

"""
给你一个数组equations，装着若干字符串表示的算式。每个算式equations[i]长度都是 4，而且只有这两种情况：a==b或者a!=b，其中a,b可以是任意小写字母。
你写一个算法，如果equations中所有算式都不会互相冲突，返回 true，否则返回 false。

比如说，输入["a==b","b!=c","c==a"]，算法返回 false，因为这三个算式不可能同时正确。

再比如，输入["c==c","b==d","x!=z"]，算法返回 true，因为这三个算式并不会造成逻辑冲突。
"""


class UnionFind:

    def __init__(self):
        self.parents = {}

    def find(self, x: str) -> int:
        if x not in self.parents:
            self.parents[x] = x
            return x
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y) -> None:
        x, y = self.find(x), self.find(y)
        if x != y:
            self.parents[x] = y


class Solution:
    def validEquation(self, equations: List[List]):
        if not equations: return False

        uf = UnionFind()

        for eq in equations:
            if eq[1] == "=":
                x, y = eq[0], eq[3]
                uf.union(x, y)

        for eq in equations:
            if eq[1] == "!":
                x, y = eq[0], eq[3]
                if uf.find(x) == uf.find(y):
                    return False

        return True


class UnitTest(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_equations_valid(self):
        self.assertEqual(True, self.s.validEquation(["c==c", "b==d", "x!=z"]))

    def test_equation_invalid(self):
        self.assertEqual(False, self.s.validEquation(["a==b", "b!=c", "c==a"]))
