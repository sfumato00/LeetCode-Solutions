"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

from python.commons import Node


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        mem = {}

        def clone(u):
            if not node:
                return None

            if u.val in mem:
                return mem[u.val]

            cloned = Node(u.val)
            mem[u.val] = cloned
            cloned.neighbors.extend([clone(v) for v in u.neighbors])
            return cloned

        return clone(node)
