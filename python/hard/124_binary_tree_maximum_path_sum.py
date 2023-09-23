# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import inf
from typing import Optional

from commons import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf

        def max_path_sum(root):
            nonlocal ans
            if not root:
                return 0

            left = max(0, max_path_sum(root.left))
            right = max(0, max_path_sum(root.right))
            ans = max(ans, left + root.val + right)
            return max(left + root.val, right + root.val)

        max_path_sum(root)
        return ans
