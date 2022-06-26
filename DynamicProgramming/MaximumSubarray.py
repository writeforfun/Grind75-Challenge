'''
Title: 53. Maximum Subarray
Level: Easy
Link: https://leetcode.com/problems/maximum-subarray/
Author: Yuan
Date: 2022/06/26
'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if max(nums) < 0:
            return max(nums)
        
        local_max, global_max = 0, 0
        
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(local_max, global_max)
            
        return global_max