from typing import Optional


class _Node:
    def __init__(self, key=0, val=0, _prev=None, _next=None):
        self.key = key
        self.val = val
        self.prev = _prev
        self.next = _next


class LRUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = _Node(), _Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.count = 0
        self.data = {}

    def get(self, key: int) -> int:
        node = self._get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self._get_node(key)
        if not node:
            node = _Node(key)
            self.data[key] = node
            self._add(node)
            if self.count + 1 > self.capacity:
                self._evict()
            else:
                self.count += 1
        node.val = value

    def is_empty(self):
        return self.head.next == self.tail

    def _add(self, node: _Node) -> None:
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _get_node(self, key: int) -> Optional[_Node]:
        if key in self.data:
            node = self.data[key]
            self._remove(node)
            self._add(node)
            return node

    def _evict(self):
        if self.is_empty():
            return
        node = self.tail.prev
        del self.data[node.key]
        self._remove(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
