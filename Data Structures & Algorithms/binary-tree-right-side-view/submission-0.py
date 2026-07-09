from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        self.bfs(root, result)
        return result
    
    def bfs(self, node:Optional[TreeNode], result:List[TreeNode]) -> None:
        level = 0
        queue = deque([(level, node)])
        while len(queue) > 0:
            # print("queue at start",queue)
            currentLevel, currentNode = queue.popleft()
            if len(queue) > 0:
                nextLevel, nextNode = queue[0]
                if nextLevel > currentLevel:
                    result.append(currentNode.val)
            else:
                result.append(currentNode.val)
            if currentNode.left:
                queue.append((currentLevel + 1, currentNode.left))
            if currentNode.right:
                queue.append((currentLevel + 1, currentNode.right))

            
        