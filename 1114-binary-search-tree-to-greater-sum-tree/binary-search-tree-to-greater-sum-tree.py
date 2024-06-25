# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        values = set()

        def dfs(node):
            if not node:
                return
            values.add(node.val)
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        def greater_sum(node):
            if not node:
                return 
            node.val += sum(val for val in values if val > node.val)
            greater_sum(node.left)
            greater_sum(node.right)

        greater_sum(root)

        return root