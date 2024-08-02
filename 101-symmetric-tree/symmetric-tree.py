# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = [(root.left, root.right)]
        
        while stack:
            left_node, right_node = stack.pop()
            
            if not left_node and not right_node:
                continue
            
            if not left_node or not right_node or left_node.val != right_node.val:
                return False
            
            stack.append((left_node.left, right_node.right))
            stack.append((left_node.right, right_node.left))
        
        return True
