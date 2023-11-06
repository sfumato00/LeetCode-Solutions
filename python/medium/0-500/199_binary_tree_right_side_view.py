# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

from python.commons import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq = deque([root])
        ans = []
        while dq:
            n = len(dq)
            for _ in range(n):
                curr = dq.popleft()
                if curr.left:
                    dq += [curr.left]
                if curr.right:
                    dq += [curr.right]
            ans += [curr.val]
        return ans
