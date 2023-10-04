from typing import Optional, Tuple


class Node:
    def __init__(self, key: int, value: int, next=None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self, size=1_000):
        self.data = [None] * size
        self.size = size

    def put(self, key: int, value: int) -> None:
        prev, head = self._search(key)

        if head:
            head.value = value
        elif prev:
            prev.next = Node(key, value)
        else:
            self.data[self._hash(key)] = Node(key, value)

    def get(self, key: int) -> int:
        _, head = self._search(key)
        return head.value if head else -1

    def remove(self, key: int) -> None:
        prev, head = self._search(key)

        if not head:
            return

        if head and prev:
            prev.next = head.next
        elif not prev:
            self.data[self._hash(key)] = head.next

    def _hash(self, key: int) -> int:
        return key % self.size

    def _search(self, key: int) -> Tuple[Optional[Node], Optional[Node]]:
        _key = self._hash(key)
        prev, head = None, self.data[_key]

        while head and head.key != key:
            prev, head = head, head.next
        return (prev, head)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
