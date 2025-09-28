#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode()
        dummy = l
        c = 0
        
        while l1 or l2 or c != 0:
            s = ((l1.val + l2.val if l1 and l2 else l1.val if l1 else l2.val if l2 else 0) + c) % 10
            c = ((l1.val + l2.val if l1 and l2 else l1.val if l1 else l2.val if l2 else 0) + c) // 10
            
            dummy.next = ListNode(s)
            dummy = dummy.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return l.next
            
        
# @lc code=end

