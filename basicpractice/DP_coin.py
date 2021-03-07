# coding=utf-8
'''
假设我们有几种不同币值的硬币 v1，v2，……，vn（单位是元）。
如果我们要支付 w 元，求最少需要多少个硬币。
比如，我们有 3 种不同的硬币，1 元、3 元、5 元，我们要支付 9 元，最少需要 3 个硬币（3 个 3 元的硬币）。
状态转移方程 f(n) = 1 + min(f(n-5), f(n-3), f(n-1))
'''


def f(n):
    if n <= 0:
        return float("inf")
    if n == 5:
        return 1
    if n == 3:
        return 1
    if n == 1:
        return 1

    return 1 + min(f(n - 5), f(n - 3), f(n - 1))

print f(9)
