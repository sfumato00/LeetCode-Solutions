# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from python.commons import TreeNode


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self.to_left_leaf(root)

    def next(self) -> int:
        curr = self.stk.pop()
        if curr.right:
            self.to_left_leaf(curr.right)
        return curr.val

    def hasNext(self) -> bool:
        return len(self.stk)

    def to_left_leaf(self, root) -> None:
        while root:
            self.stk += [root]
            root = root.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
