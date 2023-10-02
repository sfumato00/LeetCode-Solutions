from python.commons import TreeNode


def create_bst(values, lo, hi):
    if lo >= hi:
        return None

    mid = (lo + hi) // 2
    root = TreeNode(values[mid])
    root.left = create_bst(values, lo, mid)
    root.right = create_bst(values, mid + 1, hi)
    return root


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # in_order traverse
        stk, values = [], []
        curr = root
        while curr or stk:
            if curr:
                stk += [curr]
                curr = curr.left
            else:
                curr = stk.pop()
                values += [curr.val]
                curr = curr.right

        return create_bst(values, 0, len(values))


class _Iterator:
    def __init__(self, root):
        self.stk = []
        self._to_left_leaf(root)

    def next(self):
        curr = self.stk.pop()
        if curr.right:
            self._to_left_leaf(curr.right)
        return curr.val

    def has_next(self):
        return len(self.stk) > 0

    def _to_left_leaf(self, root):
        while root:
            self.stk += [root]
            root = root.left


class Solution2:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        it = _Iterator(root)
        values = []
        while it.has_next():
            values += [it.next()]
        return create_bst(values, 0, len(values))
