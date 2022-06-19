'''
Title: 169. Majority Element
Level: Easy
Link: https://leetcode.com/problems/majority-element/
Author: Yuan
Date: 2022/06/19
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        element_dict = {}
        
        for element in nums:
            if element not in element_dict:
                element_dict[element] = 1
            else:
                element_dict[element] += 1
                
        for key, value in element_dict.items():
            if value > len(nums)/2:
                return key