import unittest
from collections import deque, defaultdict

'''
这是一个面试题，在一个Excel里面有 AA 到 ZZ ，00 ~ 99 的格子范围
格子里面有的有数值，有的有表达式，评估一下，表达式是否可以计算出来。

题干不明显，但是如果能看出来，如果单元格引用有环的话，就不能计算。这道题目就可以这么解。下面是拓扑的解法

'''


def check(input):
    if not input or len(input) == 0: return True
    h, w = 100, 26 * 26

    l = w * h

    indegres = [0] * l
    adj = defaultdict(list)

    # initial adj and indegress
    def getidx(s):
        if not s or len(s) != 4: return -1
        return int(s[2:4]) * w + getcolidx(s[0:2])

    def getcolidx(s):
        if not s or len(s) != 2: return -1
        return (ord(s[0]) - ord('A')) * 26 + ord(s[1]) - ord('A')

    for k, v in input.items():
        if v.isdigit():  # digit, skip
            continue
        else:
            key = ""
            for c in v:
                if c.isalnum():
                    key += c
                else:
                    if key:
                        k2 = getidx(key)
                        indegres[k2] += 1
                        adj[getidx(k)].append(k2)
                    key = ""
            if key:
                k2 = getidx(key)
                indegres[k2] += 1
                adj[getidx(k)].append(k2)

    queue = deque()

    for i in range(len(indegres)):
        if indegres[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        for neighbour in adj[node]:
            indegres[neighbour] -= 1
            if indegres[neighbour] == 0:
                queue.append(neighbour)

    return sum(indegres) == 0


class ut(unittest.TestCase):
    # @unittest.skip
    def test_true(self):
        input = {
            'AA00': "10",
            'AA01': 'AA00 + AB00',
            'AB00': "15"
        }
        self.assertEqual(True, check(input))

    def test_false(self):
        input = {
            "AA00": "10",
            "AB00": "AA01",
            "AA01": "AB00"
        }
        self.assertEqual(False, check(input))

    def test_input_none(self):
        input = {
        }
        self.assertEqual(True, check(input))

    def test_input_exception(self):
        input = {
            "ABB00": "AA01",
        }
        self.assertEqual(False, check(input))


if __name__ == "__main__":
    unittest.main()
