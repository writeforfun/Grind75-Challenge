'''
Title: 242. Valid Anagram
Level: Easy
Link: https://leetcode.com/problems/valid-anagram/
Author: Yuan
Date: 2022/06/18
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        
        char_freq = {}
        
        for char_s in s:
            if char_s not in char_freq.keys():
                char_freq[char_s] = 1
            else:
                char_freq[char_s] += 1
                
        for char_t in t:
            if char_t not in char_freq.keys():
                return False
            if char_freq[char_t] == 1:
                del char_freq[char_t]
            elif char_freq[char_t] > 1:
                char_freq[char_t] -= 1
                
        return len(char_freq) == 0
