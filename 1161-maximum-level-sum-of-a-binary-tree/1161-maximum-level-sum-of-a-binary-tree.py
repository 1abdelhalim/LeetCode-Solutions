# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_sum = root.val
        best_level = 1         
        level = 1               

        curr_level = deque([root])   

        while curr_level:
            n = len(curr_level)
            curr_level_sum = 0

            for _ in range(n):        
                node = curr_level.popleft()
                curr_level_sum += node.val

                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)

            if curr_level_sum > max_level_sum:   
                max_level_sum = curr_level_sum
                best_level = level              

            level += 1                           

        return best_level                      
