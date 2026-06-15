# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthRecursive(root)
    
    def maxDepthRecursive(self, node: Optional[TreeNode]) -> int:
        # base:
        if not node:
            return 0
        else:
            return max(self.maxDepthRecursive(node.left), self.maxDepthRecursive(node.right)) + 1