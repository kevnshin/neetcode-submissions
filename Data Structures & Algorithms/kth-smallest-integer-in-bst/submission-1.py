import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        self.search(root, k, heap)
        return -heapq.heappop(heap)

    def search(self, node: Optional[TreeNode], k: int, heap) -> int:
        if not node:
            return
        heapq.heappush(heap, -node.val)
        if len(heap) > k:
            heapq.heappop(heap)
        self.search(node.left, k, heap)

        if len(heap) > k:
            return
        self.search(node.right, k, heap)


        