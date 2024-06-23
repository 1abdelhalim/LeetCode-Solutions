# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        
        def evaluate(node: TreeNode) -> bool:
            if not node:
                return False
            
            if node.val == 0:
                return False
            elif node.val == 1:
                return True
            elif node.val == 2:
                return evaluate(node.left) or evaluate(node.right)
            elif node.val == 3: 
                return evaluate(node.left) and evaluate(node.right)
            else:
                return False  
        
        return evaluate(root)