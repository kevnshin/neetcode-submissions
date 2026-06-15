# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeRecursive(root)
        return root

    def invertTreeRecursive(self, node: Optional[TreeNode]) -> None:
        if not node:
            return
        else:
            tempLeft:Optional[TreeNode] = node.left
            node.left = node.right
            node.right = tempLeft
            self.invertTreeRecursive(node.left)
            self.invertTreeRecursive(node.right)


        