# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.search(root, float("-inf"))

    def search(self, node:TreeNode, max_parent:int) -> int:
        if not node:
            return 0
        
        current_count = 1 if node.val >= max_parent else 0

        return current_count + self.search(node.left, max(max_parent, node.val)) + self.search(node.right, max(max_parent, node.val))


        