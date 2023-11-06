"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


from typing import Optional
from python.commons import Node


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        mem = {}

        p = head
        while p:
            mem[p] = Node(p.val)
            p = p.next

        p = head
        while p:
            p2 = mem[p]
            p2.next = mem.get(p.next)
            p2.random = mem.get(p.random)

            p = p.next

        return mem[head]
