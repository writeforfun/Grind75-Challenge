'''
Title: 876. Middle of the Linked List
Level: Easy
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Author: Yuan
Date: 2022/07/27
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Brute
class Solution1:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return head
        
        count_head = head
        count = 0
        
        while count_head:
            count += 1
            count_head = count_head.next  
        middle = count // 2 + 1 
        
        for i in range(middle - 1):
            head = head.next
        
        return head
            
class Solution2:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return head
        
        slow = fast = head
        
        while fast.next:
            slow = slow.next
            if fast.next.next == None:
                return slow
            fast = fast.next.next

        return slow

# best
class Solution3:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
             
        if head.next == None:
            return head
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow