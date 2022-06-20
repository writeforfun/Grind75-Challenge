'''
Title: 704. Binary Search
Level: Easy
Link: https://leetcode.com/problems/binary-search/
Author: Yuan
Date: 2022/06/18
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = 0
        right_index = len(nums) - 1
        
        while left_index <= right_index:
            midpoint = left_index + (right_index - left_index) // 2
            if target == nums[midpoint]:
                return midpoint
            elif target < nums[midpoint]:
                right_index = midpoint - 1
            else:
                left_index = midpoint + 1
        
        return -1




