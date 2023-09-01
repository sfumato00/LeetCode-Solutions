# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from commons import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #         # recursion
        #         if not head or not head.next:
        #             return head

        #         nxt = head.next
        #         newHead = self.reverseList(nxt)
        #         nxt.next = head
        #         head.next = None
        #         return newHead

        def reverse(h, t):
            prev, curr = t, h

            while curr != t:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        return reverse(head, None)
