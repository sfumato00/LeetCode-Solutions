# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        max_freq, freq = 0, 0
        curr_key = None
        modes = []

        def check(val):
            nonlocal curr_key, max_freq, freq

            if val != curr_key:
                if freq > max_freq:
                    modes.clear()
                    max_freq = freq

                if freq >= max_freq:
                    modes.append(curr_key)

                curr_key = val
                freq = 0

            freq += 1

        def in_order(root):
            if not root:
                return

            in_order(root.left)
            check(root.val)
            in_order(root.right)

        in_order(root)
        check(None)
        return modes
