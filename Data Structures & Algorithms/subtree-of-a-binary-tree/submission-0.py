# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)

    def dfs(self, ogTreeNode: Optional[TreeNode], subTreeNode: Optional[TreeNode]) -> bool:

        if not ogTreeNode:
            return False

        if self.isIdentical(ogTreeNode, subTreeNode):
            return True
        
        return self.dfs(ogTreeNode.left, subTreeNode) or self.dfs(ogTreeNode.right, subTreeNode)
        
    def isIdentical(self, ogTreeNode: Optional[TreeNode], subTreeNode: Optional[TreeNode]) -> bool:
        if not ogTreeNode or not subTreeNode:
            return not ogTreeNode and not subTreeNode
        
        return ogTreeNode.val == subTreeNode.val and self.isIdentical(ogTreeNode.left, subTreeNode.left) and self.isIdentical(ogTreeNode.right, subTreeNode.right) 
