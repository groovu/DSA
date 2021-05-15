# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val > l2.val:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        else:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
#         left = l1
#         right = l2
#         next_l = left.next
#         next_r = right.next
        
#         while left or right:
#             # if equal
#             #   doesn't matter, link them and move on.
#             #   next_l = next_l.next
#             #   left.next = right
#             #   right = right.next
#             #   next_r = right.next
#             if (left.val > right.val):
#                 # right points to left
#                 # right