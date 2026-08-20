# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    # [2, 4, 6, 8]
    # [2, 8, 4, 6]

    # [2,4,6,8,10]
    # [2, 10, 4, 8 ,6]
    # [1, 2, 3, 4, 5]
    # [1, 5, 2, 4, 3]
    # 0 stays the same
    # n - 1
    # left = 0
    # right = 0
        node = head
        count = 0
        node_map = {}
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # node = node.next
            # count += 1

        # mid = count // 2
        node2 = slow.next
        prev = slow.next = None
        # node = head
        # index = 0
        # head2 = None
        while node2:
            temp = node2.next
            node2.next = prev
            prev = node2
            node2 = temp
        
        node1 = head
        node2 = prev
        while node2:
            temp1 = node1.next
            temp2 = node2.next
            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2
        # i1 = 0
        # i2 = mid
        # node1 = head
        # node2 = head2
        # isFirstHalf = False
        # while i1 < mid or i2 < count:
        #     print("i1", i1)
        #     if not isFirstHalf:
        #         tempNode1 = node1.next
        #         node1.next = node2
        #         node1 = tempNode1
        #         i2 += 1
        #         isFirstHalf = True
        #     else:
        #         # if i1 < mid:
        #         tempNode2 = node2.next
        #         node2.next = node1
        #         node2 = tempNode2
        #         i1 += 1
        #         isFirstHalf = False
        #     break

            

        # node = head
        # n = count
        # i = 1
        # index = 1
        # print("count before", count)
        # print("node_map", node_map)

        # while count > 0:
        #     if index % 2 == 1:
        #         originalIndex = n - i
        #     else:
        #         originalIndex = i
        #         i += 1
        #     index += 1
        #     count -= 1            
        #     node.next = node_map[originalIndex]
        #     node = node.next

        