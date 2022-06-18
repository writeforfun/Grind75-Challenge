'''
Title: 125. Valid Palindrome
Level: Easy
Link: https://leetcode.com/problems/valid-palindrome/
Author: Yuan
Date: 2022/06/18
'''

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s if char.isalnum()).lower()
        return new_string == new_string[::-1]

class Solution2:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''.join(char for char in s if char.isalnum()).lower()
        
        left_pointer = 0
        right_pointer = len(new_string) - 1
        
        while (left_pointer < right_pointer):
            if new_string[left_pointer] != new_string[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
            
        return True