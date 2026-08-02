# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root)[1]
        

  
    
    def dfs(self, node:Optional[TreeNode]) -> (int, int):
        if not node.left and not node.right:
            return (1, 0)

        leftHeight, leftLongestDiam = self.dfs(node.left) if node.left else (0, 0)
        rightHeight, rightLongestDiam = self.dfs(node.right) if node.right else (0, 0)
        currentDiam = leftHeight + rightHeight
        heightToReturn = max(leftHeight, rightHeight) + 1
        diamToReturn = max(currentDiam, leftLongestDiam, rightLongestDiam)
        return (heightToReturn, diamToReturn)
    




        