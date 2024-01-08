# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from python.commons import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy, carry = ListNode(), 0
        prev, p1, p2 = dummy, l1, l2
        while p1 and p2:
            temp = p1.val + p2.val + carry
            carry, p1.val = divmod(temp, 10)
            prev.next, prev = p1, p1
            p1, p2 = p1.next, p2.next
        
        prev.next = p1 if p1 else p2
        while prev.next:
            temp = prev.next.val + carry
            carry, prev.next.val = divmod(temp, 10)
            prev = prev.next

        if carry:
            prev.next = ListNode(carry)

        return dummy.next

