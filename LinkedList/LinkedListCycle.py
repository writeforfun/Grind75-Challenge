'''
Title: 141. Linked List Cycle
Level: Easy
Link: https://leetcode.com/problems/linked-list-cycle/
Author: Yuan
Date: 2022/07/21
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = set()
        
        current_node = head
        while current_node:
            if current_node.next in seen:
                return True
            else:
                seen.add(current_node.next)
                current_node = current_node.next
        
        return False

class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False