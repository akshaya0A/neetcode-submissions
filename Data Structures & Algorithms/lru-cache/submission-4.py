class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.vals = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.vals:
            return -1
        node = self.vals[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.vals:
            node = Node(key, value)
            self.vals[key] = node
            self.insert(node)
        else:
            node = self.vals[key]
            node.val = value
            self.remove(node)
            self.insert(node)

        if len(self.vals) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.vals[lru.key]
