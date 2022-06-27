'''
Title: 50. Climb Stairs
Level: Easy
Link: https://leetcode.com/problems/climbing-stairs/
Author: Yuan
Date: 2022/06/26
'''

class Solution1:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]


class Solution2:
    def climbStairs(self, n: int) -> int:
            
        if n <= 2:
            return n
       
        prev1 = 1
        prev2 = 2
        current = 0
        for i in range(3, n+1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
            
        return current
    