class ListNode:
    '''Singly-linked list node.'''
    def __init__(self, data=0, _next=None):
        self.data = data
        self.next = _next

    def __str__(self):
        str_builder, _p = [], self
        while _p:
            str_builder += [str(_p.data)]
            _p = _p.next
        return ",".join(str_builder)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
