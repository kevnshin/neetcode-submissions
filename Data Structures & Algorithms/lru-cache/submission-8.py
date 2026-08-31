class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.head = None
#         self.tail = None
#         self.nodeMap = {}
#         self.capacity = capacity
#         # self.getCount = 0

#     def get(self, key: int) -> int:
#         self.getCount += 1
#         # if key == 3 and self.getCount > 48:
#         #     print("key", key)
#         #     print("nodeMap at start of GET", self.nodeMap)
#         #     print("self.head", self.head)
#         #     print("self.tail", self.tail)
#         if key not in self.nodeMap:
#             print("key", key)
#             # print("nodeMap at start of GET", self.nodeMap)
#             print("self.head", self.head)
#             print("self.tail", self.tail)
#             # for key in self.nodeMap:
#             #     print("key: ", key, ", val:", self.nodeMap[key].val[1])
#             return -1
#         node = self.nodeMap[key]
#         if not node or node is None:
#             return -1

#         if node == self.tail:
#             return node.val[1]

#         self.moveNodeToBack(node)
#         # if self.head == node:
#         #     self.head = self.head.next
#         # else:
#         #     ogPrev = node.prev
#         #     ogNext = node.next
#         #     ogPrev.next = ogNext
#         #     ogNext.prev = ogPrev
#         # node.next = None
#         # node.prev = self.tail
#         # self.tail.next = node
#         # self.tail = node
        

#         # case node to Move is head
#         # nodeToMove -> nodeB
#         # head = nodeToMove.next make head the next one
#         # make nodeToMove.next None
#         # make nodeToMove.prev the current tail
#         # make the current tail.next the nodeToMove
#         # make currentTail the nodetomove

#         # is in middle
#         # node A -> nodeToMove -> nodeB
#         # final node A -> nodeB -> nodeToMove
#         # get the prev node (NodeA)
#         # made the prevNode.next = nodeToMove.next
#         # get the next node (NodeB)
#         # make the nextNode.prev = the prev node (NodeA)

#         # make nodeToMove.next None
#         # make nodeToMove.prev the current tail
#         # make currentTail the nodetomove

#         # prev = node.prev
#         # if node == self.head:
#         #     self.head = node.next

#         # if prev and prev.next:
#         #     prev.next = node.next.next
#         # next = node.next
#         # if next:
#         #     next.prev = prev
#         # prevTail = self.tail
#         # prevTail.next = node
#         # node.prev = prevTail
#         # self.tail = node

#         # if key == 3 and self.getCount > 48:
#         #     print("------end of GET--------")
#         #     print("self.head", self.head)
#         #     print("self.tail", self.tail)
#         #     print("nodeMap", self.nodeMap)
#         return node.val[1]

#     def put(self, key: int, value: int) -> None:
#         if key == 3 and value == 5:
#             print("key", key)
#             print("value", value)
#             print("nodeMap at start of PUT", self.nodeMap)
#             print("self.head", self.head)
#             print("self.tail", self.tail)
#         if key in self.nodeMap:
#             if key == 3 and value == 5:
#                 print("3 found in NODEMAP")
#             node = self.nodeMap[key]
#             node.val = (key, value)
#             self.moveNodeToBack(node)
#             # if node == self.tail:
#             #     return
#             # if self.head == node:
#             #     self.head = self.head.next
#             # else:
#             #     ogPrev = node.prev
#             #     ogNext = node.next
#             #     ogPrev.next = ogNext
#             #     ogNext.prev = ogPrev
#             # node.next = None
#             # node.prev = self.tail
#             # self.tail.next = node
#             # self.tail = node
#             return
#         else:
#             if key == 3 and value == 5:
#                 print("3 NOT found in NODEMAP")
#             node = Node(val = (key, value))
#             self.nodeMap[key] = node

#         if not self.head and not self.tail:
#             self.head = node
#             self.tail = node
#             return
        
#         node.prev = self.tail
#         self.tail.next = node
#         self.tail = node


#         if len(self.nodeMap) > self.capacity:
#             nodeToRemove = self.head
#             print("removing node", nodeToRemove)
#             print("self.head", self.head)
#             print("self.tail", self.tail)
#             print("nodeMap", self.nodeMap)
#             self.head = nodeToRemove.next
#             del self.nodeMap[nodeToRemove.val[0]]
        
#         if key == 3 and value == 5:
#         # if key == 3 and self.getCount > 48:
#             print("------end of PUT--------")
#             print("self.head", self.head)
#             print("self.tail", self.tail)
#             print("self.nodeMap", self.nodeMap)

#     def moveNodeToBack(self, node:Node) -> None:
#         if self.head == node:
#             self.head = self.head.next
#         else:
#             ogPrev = node.prev
#             ogNext = node.next
#             if ogNext:
#                 ogPrev.next = ogNext
#                 ogNext.prev = ogPrev
#         node.next = None
#         node.prev = self.tail
#         self.tail.next = node
#         self.tail = node
        

# # Definition for doubly-linked list.
# class Node:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev