'''
Title: 283. Move Zeroes
Level: Easy
Link: https://leetcode.com/problems/move-zeroes/
Author: Yuan
Date: 2022/06/30
'''

class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ptr] = nums[i]
                ptr = ptr + 1
            
        for i in range(ptr, len(nums)):
            nums[i] = 0

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        left_ptr = 0
        for right_ptr in range(len(nums)):
            if nums[right_ptr] != 0:
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                left_ptr = left_ptr + 1