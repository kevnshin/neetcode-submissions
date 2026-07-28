# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Node = l1
        l2Node = l2
        dummyHead = ListNode()
        resultCurrent = dummyHead
        carryOver = 0

        while l1Node or l2Node:
            newNode = ListNode()
            if l1Node and l2Node:
                total = l1Node.val + l2Node.val + carryOver
            elif l1Node:
                total = l1Node.val + carryOver
            else:
                total = l2Node.val + carryOver

            if total >= 10:
                carryOver = 1
                currentDigit = total % 10
            else:
                carryOver = 0
                currentDigit = total

            newNode.val = currentDigit

            if l1Node:
                l1Node = l1Node.next
            if l2Node:
                l2Node = l2Node.next
            
            resultCurrent.next = newNode
            resultCurrent = resultCurrent.next
        
        if carryOver > 0:
            newNode = ListNode()
            newNode.val = carryOver
            resultCurrent.next = newNode
        
        return dummyHead.next
        
        


        