from typing import List, Optional

from commons import TreeNode


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []

        def delete(root):
            if not root:
                return None

            root.left = delete(root.left)
            root.right = delete(root.right)

            if root.val in to_delete:
                if root.left:
                    ans.append(root.left)
                if root.right:
                    ans.append(root.right)
                return None
            return root

        root = delete(root)
        if root:
            ans += [root]
        return ans
