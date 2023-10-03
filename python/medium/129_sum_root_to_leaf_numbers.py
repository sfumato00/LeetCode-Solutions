# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.commons import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr):
            if not root:
                return 0

            curr = curr * 10 + root.val

            if not root.left and not root.right:
                return curr

            total = 0
            total += dfs(root.left, curr) if root.left else 0
            total += dfs(root.right, curr) if root.right else 0
            return total

        return dfs(root, 0)
