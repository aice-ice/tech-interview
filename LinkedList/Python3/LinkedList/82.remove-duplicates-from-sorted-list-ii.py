#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = ListNode(0)
        dummy = l

        while head:
            if head.next and head.val == head.next.val:
                val = head.val
                
                while head and head.val == val:
                    head = head.next

                dummy.next = head
            else:
                dummy.next = head
                dummy = dummy.next
                head = head.next


        return l.next


# @lc code=end

