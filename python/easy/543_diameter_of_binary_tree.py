# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.commons import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            if not root:
                return 0
            nonlocal diameter
            left, right = dfs(root.left), dfs(root.right)
            if left + right > diameter:
                diameter = left + right
            return max(left, right) + 1

        dfs(root)
        return diameter
