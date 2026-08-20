"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_dummy_head = Node(x="-101")
        current_old_node = head
        current_new_node = new_dummy_head
        node_map = {}
        while current_old_node:
            # print("current_old_node.val", current_old_node.val)
            # print("current_old_node.next", current_old_node.next)
            # print("current_old_node.random", current_old_node.random)
            new_node = Node(x=current_old_node.val)
            node_map[current_old_node] = new_node
            current_new_node.next = new_node
            current_new_node = current_new_node.next
            current_old_node = current_old_node.next
        
        current_old_node = head
        current_new_node = new_dummy_head.next
        while current_old_node:
            if current_old_node.random:
                current_new_node.random = node_map[current_old_node.random]
            current_new_node = current_new_node.next
            current_old_node = current_old_node.next
        
        return new_dummy_head.next


            
        