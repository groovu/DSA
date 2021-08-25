# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head
        
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next
#         ret_head = head
#         prev = None
#         cur = head
#         # find head loops
#         while cur.val == val:
#             ret_head = head.next
#             prev = cur
#             cur = cur.next
        
#         cur
#         while cur not None:
#             if cur.val != val:
#                 cur = cur.next
                
#             if cur.val == val:
#                 cur = cur.next
#                 prev.next = cur
#                 prev = prev.next
        
#         return ret_head