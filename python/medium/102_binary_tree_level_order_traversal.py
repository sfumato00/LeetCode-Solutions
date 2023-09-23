# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

from commons import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            sz = len(q)
            ans += [[]]
            for _ in range(sz):
                curr = q.popleft()
                ans[-1] += [curr.val]
                if curr.left:
                    q += [curr.left]
                if curr.right:
                    q += [curr.right]
        return ans
