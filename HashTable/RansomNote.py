'''
Title: 383. Ransom Note
Level: Easy
Link: https://leetcode.com/problems/ransom-note/
Author: Yuan
Date: 2022/06/18
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ran_dict = {}
        
        for ran_char in ransomNote:
            if ran_char not in ran_dict.keys():
                ran_dict[ran_char] = 1
            else:
                ran_dict[ran_char] += 1
        
        for key in magazine:
            if key in ran_dict:
                ran_dict[key] -= 1
                if ran_dict[key] == 0:
                    del ran_dict[key]
                    
        return  len(ran_dict) == 0
