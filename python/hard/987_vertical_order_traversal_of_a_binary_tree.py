# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from typing import List, Optional

from python.commons import TreeNode


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        coordinate_map = defaultdict(lambda: defaultdict(list))

        def traverse(root, x, y):
            if not root:
                return

            coordinate_map[x][y] += [root.val]
            traverse(root.left, x - 1, y + 1)
            traverse(root.right, x + 1, y + 1)

        traverse(root, 0, 0)
        ans = []
        for x in sorted(coordinate_map):
            vertical_line = []
            for y in sorted(coordinate_map[x]):
                vertical_line.extend(sorted(coordinate_map[x][y]))
            ans.append(vertical_line)
        return ans
