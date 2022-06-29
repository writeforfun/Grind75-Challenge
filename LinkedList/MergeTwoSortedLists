'''
Title: 21. Merge Two Sorted Lists
Level: Easy
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Author: Yuan
Date: 2022/06/29
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = dummy = ListNode(-1)
        
        while list1  and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
                
            head = head.next
            
        if list1 == None:
            head.next = list2
        if list2 == None:
            head.next = list1
            
        return dummy.next
                