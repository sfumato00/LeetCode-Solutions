# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from commons import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head, tail):
            prev, curr = tail, head

            while curr != tail:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        dummy = ListNode(0, head)
        slow = dummy
        while slow:
            fast = slow
            for _ in range(k):
                if not fast or not fast.next:
                    return dummy.next
                fast = fast.next
            temp = slow.next
            slow.next = reverse(slow.next, fast.next)
            slow = temp

        return dummy.next
