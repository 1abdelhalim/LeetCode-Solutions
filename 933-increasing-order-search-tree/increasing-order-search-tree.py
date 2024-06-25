# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
    
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        
        dfs(root)

        def toSkewedTree(values):
            if not values:
                return None
            
            root = TreeNode(values[0])
            current = root

            for val in values[1:]:
                current.right = TreeNode(val)
                current = current.right
            
            return root
        
        return toSkewedTree(stack)





        
        