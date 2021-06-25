# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        
        def traverse(node):
            i = 1
            val = 0
            while node:
                val += node.val * i
                i *= 10
                node = node.next
            return val
        def build(num):
            head = ListNode()
            curr = head
            while num != 0:
                val = num % 10
                curr.val = val
                if num // 10 != 0:
                    curr.next = ListNode()
                curr = curr.next
                num = num //10
                print(num)
            return head
        num1 = traverse(l1)
        num2 = traverse(l2)
        total = num1 + num2
        
        return build(total)