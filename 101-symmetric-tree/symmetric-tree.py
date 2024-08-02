# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check_mirror(left_node, right_node):
            if not left_node and not right_node:
                return True 

            if not left_node or not right_node:
                return False

            return (left_node.val == right_node.val 
                and check_mirror(left_node.left, right_node.right)
                and check_mirror(left_node.right, right_node.left)
                )

        return check_mirror(root, root)