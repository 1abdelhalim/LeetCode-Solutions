# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node_orig: TreeNode, node_cloned: TreeNode) -> TreeNode:
            if not node_orig:
                return None
            if node_orig is target:
                return node_cloned
            left_result = dfs(node_orig.left, node_cloned.left)
            if left_result:
                return left_result
            return dfs(node_orig.right, node_cloned.right)
        
        return dfs(original, cloned)
