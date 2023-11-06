# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

from python.commons import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mem = {x: i for i, x in enumerate(inorder)}
        r, n = 0, len(preorder)

        def build(lo, hi):
            nonlocal r
            if r == n:
                return None

            val = preorder[r]
            pos = mem[val]

            if pos < lo or pos > hi:
                return None

            r += 1
            root = TreeNode(val)
            root.left = build(lo, pos - 1)
            root.right = build(pos + 1, hi)
            return root

        return build(0, n - 1)
