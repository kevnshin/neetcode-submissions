# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet:Set[ListNode] = set()
        current:Optional[ListNode] = head
        while current:
            if current in nodeSet:
                return True
            nodeSet.add(current)
            current = current.next
        return False
        
        