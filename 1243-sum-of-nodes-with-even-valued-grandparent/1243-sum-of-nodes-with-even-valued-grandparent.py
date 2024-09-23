# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        sum = 0 
        
        def dfs(node):
            nonlocal sum
            if not node:
                return
            
            if node.val % 2 == 0:
                if node.right:
                    if node.right.right:
                        sum += node.right.right.val
                    if node.right.left:
                        sum += node.right.left.val
                
                if node.left:
                    if node.left.right:
                        sum += node.left.right.val
                    if node.left.left:
                        sum += node.left.left.val

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return sum
