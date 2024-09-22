# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # step 1 we need to count all nodes with a condtion 
        # for each node we need the sum and n of nodes in the subtree 
        # dfs for traversing  with a recursion func for calc 
        # if rec val == node.val -> count += 1  

        count = 0 

        def postorder(node):
            if not node:
                return (0, 0) 

            nonlocal count 

            left_sum, left_count = postorder(node.left)
            right_sum, right_count = postorder(node.right)

            subtree_sum = left_sum + right_sum + node.val
            node_count = left_count + right_count + 1

            if node.val == subtree_sum // node_count:
                count += 1  

            return subtree_sum, node_count

        postorder(root) 
        return count  



        