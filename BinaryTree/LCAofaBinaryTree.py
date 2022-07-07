'''
Title: 235. Lowest Common Ancestor of a Binary Search Tree
Level: Easy
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
Author: Yuan
Date: 2022/07/7
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root.val == None:
            return root.val
        
        current_node = root
        while current_node:
            if p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left 
            elif p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            else:
                return current_node