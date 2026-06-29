# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True

        return self.height(root)[0]

    def height(self, node: Optional[TreeNode]) -> bool:
        if node:
            leftBalanced, leftHeight = self.height(node.left)
            rightBalanced, rightHeight = self.height(node.right)
            return (leftBalanced and rightBalanced and abs(leftHeight - rightHeight) <= 1, 1 + max(leftHeight, rightHeight))
        else:
            return (True, 0)
        