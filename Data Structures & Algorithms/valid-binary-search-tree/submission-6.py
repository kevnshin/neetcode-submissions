# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.search(root, float("-inf"), float("inf"))

    def search(self, node: Optional[TreeNode], left_bound: int, right_bound:int) -> bool:
        if not node:
            return True
        if not left_bound < node.val < right_bound:
            return False
        return self.search(node.left, left_bound, node.val) and self.search(node.right, node.val, right_bound)

        

        