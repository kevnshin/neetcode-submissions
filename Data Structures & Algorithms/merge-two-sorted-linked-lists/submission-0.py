# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current_list1:ListNode = list1
        current_list2:ListNode = list2
        head:ListNode = None
        current_combined:ListNode = None

        # insight is you don't need to iterate through every element if you run out of one list first
        # cause that means the rest of the other list is all larger so can just add those at once
        while current_list1 and current_list2:
            temp_new_node:ListNode = None
            if current_list1.val < current_list2.val:
                temp_new_node = current_list1
                current_list1 = current_list1.next
            else:
                temp_new_node = current_list2
                current_list2 = current_list2.next
            
            if not head:
                head = temp_new_node
                current_combined = head
            else:
                current_combined.next = temp_new_node
                current_combined = current_combined.next
        
        temp_new_node:ListNode = current_list1 if current_list1 else current_list2
        if not head:
            head = temp_new_node
        else:
            current_combined.next = temp_new_node

        return head
