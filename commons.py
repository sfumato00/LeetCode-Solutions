# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        sb, p = [], self
        while p:
            sb += [str(p.val)]
            p = p.next
        return ",".join(sb)