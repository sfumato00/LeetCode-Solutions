class Node:
    def __init__(self, key, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev, self.next = prev, next

    def __str__(self):
        sb, p = [], self
        while p:
            sb.append(f"({p.key}:{p.value})")
            p = p.next
        return ",".join(sb)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head, self.tail = Node("head"), Node("tail")
        self.head.next, self.tail.prev = self.tail, self.head
        self.data = {}

    def add(self, node: Node):
        prev, nxt = self.head, self.head.next
        node.prev, node.next = prev, nxt
        prev.next, nxt.prev = node, node

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        node = self.data.get(key, None)
        if not node:
            return -1

        self.remove(node)
        self.add(node)
        print(self.head)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.data.get(key, Node(key, value))
        if key not in self.data:
            self.data[key] = node
        else:
            node.value = value
            self.remove(node)
        self.add(node)

        if len(self.data) > self.capacity:
            to_delete = self.tail.prev
            self.remove(to_delete)
            self.data.pop(to_delete.key)

        print(self.head)
