class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(val=(0, 0))
        self.tail = Node(val=(0, 0))
        self.cache = {}
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.removeFromList(node)
        self.addToList(node)
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.removeFromList(node)
            node.val = (key, value)
        else:
            node = Node(val = (key, value))
        self.cache[key] = node
        self.addToList(node)

        if len(self.cache) > self.capacity:
            nodeToRemove = self.head.next
            self.removeFromList(nodeToRemove)
            del self.cache[nodeToRemove.val[0]]
        
    def removeFromList(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def addToList(self, node: Node) -> None:
        prev = self.tail.prev
        nxt = self.tail
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

class Node:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
