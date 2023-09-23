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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, _min, _max):
            if not root:
                return True

            if _min < root.val < _max:
                return isValid(root.left, _min, root.val) and isValid(
                    root.right, root.val, _max
                )
            return False

        return isValid(root, -inf, inf)
