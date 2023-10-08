# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.commons import TreeNode


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return None

        left = root.left
        right = root.right

        left_tail = self.flatten(left)
        right_tail = self.flatten(right)

        root.left = None
        if left_tail:
            left_tail.right = right
            root.right = left

        return right_tail if right else left_tail if left else root
