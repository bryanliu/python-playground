import functools
import cProfile
import unittest

class Solution:
    #recursive + memo
    def fib(self, k):

        fib = [1] * 2

        while True:
            a = fib[-1] + fib[-2]
            if a > k:
                break
            else:
                fib.append(a)

        fib.reverse()
        print(fib)
        n = len(fib)
        @functools.lru_cache(None)
        def backtrade(rest):
            #print(rest)
            if rest == 0:
                return 0
            ans = float('inf')
            for i in range(n):
                curr = fib[i]
                if curr > rest:
                    continue
                ans = min(ans, backtrade(rest - curr))

            return ans + 1

        res = backtrade(k)
        print(res)
        return res


    #dp
    def fib2(self, k):
        if k < 1: return 0
        fib = [1] * 2

        while True:
            a = fib[-1] + fib[-2]
            if a > k:
                break
            else:
                fib.append(a)

        dp = [float('inf')] * (k+1) #dp[i] means how many fibs need for this number i

        dp[0] = 1 #0, nothing to choose, only 1 possible result
        n = len(dp)
        for i in range(1, n):

            for c in fib:
                if c == i:
                    dp[i] = 1 #if equal to fib[c], the count is lowest, which is one
                    break
                else:
                    if i>=c:
                        dp[i] = min(dp[i], dp[i-c]+1) #choose the lowest from previous result
        print(dp[-1])
        return dp[-1]

    # value = "20"
    # print(f"run for k={value}")
    # #using cProfile to measure the proformance
    # print("recursive:")
    # cProfile.run("fib("+value+")")
    # print("dp")
    # cProfile.run("fib2("+value+")")

class Test(unittest.TestCase):

 def test_coin(self):
     s = Solution()
     self.assertEqual(3, s.fib(19))
     self.assertEqual(2, s.fib(7))
     self.assertEqual(2, s.fib(10))
     self.assertEqual(7, s.fib(20000))

if __name__ == '__main__':
    unittest.main()

'''
k=20000
with recursive + memo, the proformace are almost the same. without memo, recursive will take 60+ seconds for only k=19
7
         413702 function calls (393702 primitive calls) in 0.209 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.209    0.209 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 functools.py:35(update_wrapper)
        1    0.000    0.000    0.000    0.000 functools.py:478(lru_cache)
        1    0.000    0.000    0.000    0.000 functools.py:517(decorating_function)
  20001/1    0.129    0.000    0.209    0.209 testtest:18(backtrade)
        1    0.000    0.000    0.209    0.209 testtest:4(fib)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.callable}
        1    0.000    0.000    0.209    0.209 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   393655    0.080    0.000    0.080    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}


7
         393659 function calls in 0.216 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.216    0.216 <string>:1(<module>)
        1    0.127    0.127    0.216    0.216 testtest:37(fib2)
        1    0.000    0.000    0.216    0.216 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   393633    0.089    0.000    0.089    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       20    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


run for k=19
recursive:
[13, 8, 5, 3, 2, 1, 1]
3
         149340774 function calls (74670394 primitive calls) in 71.922 seconds
#you can see massive function calls here. most of these are all duplicate calls for same sub-problelm.
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   71.922   71.922 <string>:1(<module>)
74670381/1   55.217    0.000   71.922   71.922 Coin_DP.py:20(backtrade)
        1    0.000    0.000   71.922   71.922 Coin_DP.py:5(fib)
        1    0.000    0.000   71.922   71.922 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
 74670380   16.705    0.000   16.705    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'reverse' of 'list' objects}


dp
3
         111 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 Coin_DP.py:38(fib2)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
      100    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        5    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

when k=9000000, resursive is a little bit slower then dp because of the recursive call cost (up is recursive)
         300069742 function calls (291069742 primitive calls) in 161.043 seconds
         291069687 function calls in 150.179 seconds
'''








