'''
Title: 509. Fibonacci Number
Level: Easy
Link: https://leetcode.com/problems/fibonacci-number/
Author: Yuan
Date: 2022/06/27
Note: Not in Grind 75
'''


# dp with list
class Solution1:
    def fib(self, n: int) -> int:
        
        dp = [0, 1, 1]
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]

# dp with dictionary
class Solution2:
    def fib(self, n: int) -> int:
        
        dp ={0:0, 1:1, 2:1}

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

# recursive
class Solution3:
    def fib(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)


