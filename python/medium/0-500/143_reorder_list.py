# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

from python.commons import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # locate middle point
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        i = 0
        while fast:
            if i % 2 == 1:
                slow = slow.next
            fast = fast.next
            i += 1

        head2 = slow.next
        slow.next = None

        # reverse
        prev, curr = None, head2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head2 = prev

        # merge
        p1, p2 = head, head2
        while p1 and p2:
            temp1 = p1.next
            temp2 = p2.next
            p1.next = p2
            p2.next = temp1
            p1 = temp1
            p2 = temp2
        return head
