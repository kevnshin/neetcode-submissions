# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        current_gap:int = 0
        dummy = ListNode(0)
        dummy.next = head
        slow_pointer:Optional[ListNode] = dummy
        fast_pointer:Optional[ListNode] = dummy

        while fast_pointer:
            if current_gap != n:
                fast_pointer = fast_pointer.next
                current_gap += 1
            else:
                fast_pointer = fast_pointer.next
                if fast_pointer:
                    slow_pointer = slow_pointer.next
        slow_pointer.next = slow_pointer.next.next

        return dummy.next
        