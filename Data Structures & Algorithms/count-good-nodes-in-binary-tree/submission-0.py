# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#       3
#      /
#     3
#    / \
#   4   2

  

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.search(root, float("-inf"))

    def search(self, node:TreeNode, max_parent:int) -> int:
        # print("\n-----SEARCH-----")
        if not node:
            # print("empty node")
            return 0
        
        # print("node", node.val)
        # print("max_parent", max_parent)
        
        current_count = 1 if node.val >= max_parent else 0
        # print("current_count", current_count)

        return current_count + self.search(node.left, max(max_parent, node.val)) + self.search(node.right, max(max_parent, node.val))


        