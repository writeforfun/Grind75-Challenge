'''
Title: 278. First Bad Version
Level: Easy
Link: https://leetcode.com/problems/first-bad-version/
Author: Yuan
Date: 2022/06/20
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            midpoint = left + (right -left) // 2
            if isBadVersion(midpoint) == False:
                left = midpoint + 1
            else:
                right = midpoint
                
        return left




