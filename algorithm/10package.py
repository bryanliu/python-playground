# 第一个 DP 实现，
import unittest


def printmatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

    print("\n")


def knpackage_state_matrix(itemsweights, maxload):
    n = len(itemsweights)
    states = [[0 for i in range(maxload + 1)] for j in range(n)]  # +1 表示不装的情况

    # printmatrix(states)

    # 预处理第一个Item
    states[0][0] = 1
    states[0][itemsweights[0]] = 1

    # printmatrix(states)

    for i in range(1, n):
        for j in range(len(states[i])):
            if states[i - 1][j] == 1:  # not load this item
                states[i][j] = states[i - 1][j]

        weight = itemsweights[i]
        for j in range(len(states[i]) - weight):  # load this item
            if states[i - 1][j] == 1:
                states[i][j + weight] = 1
    printmatrix(states)
    i = len(states[-1]) - 1

    max_weight = None

    while i >= 0:  # 找最大值
        if states[-1][i] == 1:
            max_weight = i  # found the max weight
            break
        i -= 1

    if max_weight == None:
        print("不能找到最大值")

    # 回溯商品选择
    i = len(itemsweights) - 1
    j = max_weight
    while i > 0:
        if j - itemsweights[i] >= 0 and states[i - 1][j - itemsweights[i]] == 1:
            print("choose product", i + 1)
            j = j - itemsweights[i]
        i -= 1
    if j > 0: print("choose product 1")  # for item1, if not 0, then it means choose this one

    return max_weight


def knpackage_state_single_row(itemweights, maxload):
    """
    时间复杂度 O(n*w) 空间复杂度 O(w), 比上面一个更节省空间
    """
    states = [0 for i in range(maxload + 1)]
    # handle first row
    states[0] = 1
    states[itemweights[0]] = 1

    for i in range(1, len(itemweights)):

        weight = itemweights[i]

        j = len(states) - weight - 1

        while j >= 0:
            if states[j] == 1:
                states[j + weight] = 1
            j -= 1

        print(states)


def knpackage_with_value(itemweights, values, maxload):
    states = [0 for i in range(maxload + 1)]
    states[itemweights[0]] = values[0]

    for i in range(1, len(itemweights)):
        weight = itemweights[i]
        j = len(states) - 1
        while j >= weight:
            # add the current value with previous value
            states[j] = max(states[j], states[j - weight] + values[i])
            j -= 1
    print(states)
    return states[-1]


def f(i, currentload, itemweight, maxallowload):
    '''

    :param i: 当前元素
    :param currentload: 当前装到包中的重量
    :param n: 总共的物品数量
    :return: 目前装到包中的最大值
    '''
    n = len(itemweight)
    if i == n or currentload == maxallowload:
        # 如果过了所有的商品，或者达到了最大值，返回
        return currentload

    l1 = f(i + 1, currentload, itemweight, maxallowload)  # 不选择这个商品

    if currentload + itemweight[i] <= maxallowload:
        l2 = f(i + 1, currentload + itemweight[i], itemweight, maxallowload)
    else:
        l2 = currentload
    return max(l1, l2)


def knpackage_backtrack(itemweight, maxallowload):
    maxvalue = f(0, 0, itemweight, maxallowload)
    print(maxvalue)


def fullpackage_with_value_n3(weights, values, size):
    """
    完全背包问题，对于每一个商品，都可以放无数个
    教程，极客时间 https://time.geekbang.org/column/article/291638
    这是一个n的三次方的解
    :param weights:
    :param values:
    :param size:
    :return:
    """
    h = len(weights)
    w = size + 1
    dp = [[0] * (size + 1) for _ in range(h)]
    w1 = weights[0]
    for i in range(0, w):
        if i + w1 < w:  # 只要不大于边界，都可以放进去
            dp[0][i + w1] = values[0]
        else:
            break

    for i in range(1, h):
        for j in range(w):
            weight = weights[i]
            dp[i][j] = dp[i - 1][j]  # copy from above
            n = j // weight
            for k in range(n + 1):  # 边界到n，所以这边得n+1
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * weight] + values[i] * k)
    for l in dp:
        print(l)
    return dp[-1][-1]


def fullpackage_with_value_n2(weights, values, size):
    """
    这是一个空间复杂度只有n的平方的解，比fullpackage_with_value_n3 复杂度要低.
    晕，原来凑硬币2就是完全背包问题，并且按照 https://leetcode-cn.com/problems/coin-change-2/ 的思路，空间复杂度做了压缩
    :param weights:
    :param values:
    :param size:
    :return:
    """
    h, w = len(weights), size + 1
    dp = [0] * w  # 只需要一维数组就够了

    w0 = weights[0]
    for i in range(w):  # 初始化第一行
        if i + w0 < w:
            dp[i + w0] = values[0]

    for i in range(1, h):
        weight = weights[i]
        for j in range(weight, w):
            dp[j] = max(dp[j], dp[j - weight] + values[i])

    return dp[-1]


class Test(unittest.TestCase):
    @unittest.skip("don't run this now")
    def test_01withvalue(self):
        self.assertEqual(18, knpackage_with_value([2, 2, 4, 6, 3], [3, 4, 8, 9, 6], 9))
        self.assertEqual(8, knpackage_with_value([0, 3, 2, 1], [0, 5, 2, 3], 5))
        self.assertEqual(12, knpackage_with_value([1, 2, 1, 7, 9, 4], [1, 2, 1, 7, 9, 4], 12))
        self.assertEqual(73, knpackage_with_value([31, 26, 33, 21, 40], [31, 26, 33, 21, 40], 75))

    def test_fullpackage(self):
        self.assertEqual(15, fullpackage_with_value_n3([3, 2, 1], [5, 2, 3], 5))
        self.assertEqual(15, fullpackage_with_value_n2([3, 2, 1], [5, 2, 3], 5))


if __name__ == "__main__":
    unittest.main()

# print( knpackage_state_single_row([2,2,4,6,3], 10))
# print knpackage_state_matrix([4,6,3,2,2], 9)
# print(knpackage_with_value([2,2,4,6,3], [3,4,8,9,6], 9))
# knpackage_backtrack([2,2,4,6,3], 10)
