# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodes = set()
        
        node_a = headA
        while node_a:
            nodes.add(node_a)
            node_a = node_a.next
        
        node_b = headB
        while node_b:
            if node_b in nodes:
                return node_b
            node_b = node_b.next
        return None