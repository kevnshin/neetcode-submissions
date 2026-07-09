from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        starting_level = 0
        queue = deque([(starting_level, root)])
        result = []
        if not root:
            return result
        while len(queue) > 0:
            level, node = queue.popleft()
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        return result

            

        