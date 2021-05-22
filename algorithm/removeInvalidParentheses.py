import unittest

'''
301. 删除无效的括号 https://leetcode-cn.com/problems/remove-invalid-parentheses/
给你一个由若干括号和字母组成的字符串 s ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 任意顺序 返回。
'''


def removeInvalidParentheses(s):
    def validate(s):
        left = right = 0

        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                right += 1
            if left < right:
                return False
        return left == right

    level = [s]
    while level:
        # print(level)
        res = list(filter(validate, level))
        if res:
            return res
        else:

            level2 = set()
            for s1 in level:
                for i in range(len(s1)):
                    if s1[i] in "()":
                        level2.add(s1[:i] + s1[i + 1:])
            level = level2

    return []


class ut(unittest.TestCase):

    def test_success(self):
        res = sorted(removeInvalidParentheses("(a)())()"))
        self.assertEqual(sorted(["(a)()()", "(a())()"]), res)

    def test_empty(self):
        self.assertEqual([""], removeInvalidParentheses(")("))


if __name__ == '__main__':
    unittest.main()
