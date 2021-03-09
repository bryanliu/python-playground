'''
https://leetcode-cn.com/problems/longest-palindromic-substring/
5. 最长回文子串 给你一个字符串 s，找到 s 中最长的回文子串。
'''
import cProfile


def centralextent(s):
    n = len(s)
    res = 0
    def helper(i, j):
        while i>=0 and j < n:
            if s[i] == s[j]:
                min(1, 2)#纯计数，
                i -= 1
                j +=1
            else:
                break
        nonlocal res
        res = max(res, j-i-1)
        #print(res)

    for i in range(n):
        helper(i, i)
        helper(i, i+1)

    print("longest palidrome", res)

def dp_ij(s):
    n = len(s)
    res = 0
    dp = [[True] * n for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            min(1, 2)#纯计数
            dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
            if dp[i][j]:
                res = max(res, j-i+1)
    print("dp longest palidrome", res)



s = "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbaba" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "babadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabadbabad" \
    "dbabadbabadbabadbabad"
cProfile.run(f"centralextent('{s}')")
cProfile.run(f"dp_ij('{s}')")
#dp_ij(s)

