# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        flag = 1
        
        while queue:
            level_size = len(queue)
            level = deque()
            
            for i in range(level_size):
                node = queue.popleft()
                
                if flag:
                    level.append(node.val)  
                else:
                    level.appendleft(node.val)  
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(list(level))
            flag = 1 - flag  
        
        return result



        