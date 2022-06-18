'''
Title: 1. Two Sum
Level: Easy
Link: https://leetcode.com/problems/two-sum/
Author: Yuan
Date: 2022/06/18
'''

class SolutionHashTable:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #apply hash table
        hash_table = {}
        for i, n in enumerate(nums):
            if target - n in hash_table:
                return [hash_table[target - n], i]
            hash_table[n] = i


class SolutionBrute:
    def twoSum(self, nums, target):
        ans = 0
        for index_of_num1 in range(0, len(nums)):
            ans = target - nums[index_of_num1]
            for index_of_num2 in range(index_of_num1+1, len(nums)):
                if nums[index_of_num2] == ans:
                    return [index_of_num1, index_of_num2]