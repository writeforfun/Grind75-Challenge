'''
Title: 217. Contains Duplicate
Level: Easy
Link: https://leetcode.com/problems/contains-duplicate/
Author: Yuan
Date: 2022/06/19
'''

# Build hast table and loop it 
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        element_dict = {}
        
        for element in nums:
            if element not in element_dict.keys():
                element_dict[element] = 1
            else:
                element_dict[element] += 1
                
        for value in element_dict.values():
            if value > 1:
                return True
        
        return False
        
# Build hash table and access directly (faster than Solution1)
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        element_dict = {}
        
        for element in nums:
            if element in element_dict.keys():
                return True
            if element not in element_dict.keys():
                element_dict[element] = 1
        
        return False
        
# Sort the input array and compare the elements next to each other.
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums [i+1]:
                return True
            
        return False