'''
Title: 20. Valid Parentheses
Level: Easy
Link: https://leetcode.com/problems/valid-parentheses/
Author: Yuan
Date: 2022/06/18
'''

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"(": ")", "[": "]", "{": "}"}
        stack = []
        
        for element in s:
            if element in brackets.keys():
                stack.append(element)
            if element in brackets.values():
                if len(stack) == 0:
                    return False
                top_of_stack = stack.pop()
                if brackets[top_of_stack] != element:
                    return False
                
        return len(stack) == 0

solution = Solution()
print(solution.isValid("()[]{}")) # True
print(solution.isValid("(]")) # False