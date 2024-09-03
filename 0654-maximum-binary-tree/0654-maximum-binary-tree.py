# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for num in nums:
            current_node = TreeNode(num)

            while stack and stack[-1].val < num:
                current_node.left = stack.pop()

            if stack:
                stack[-1].right = current_node

            stack.append(current_node)

        return stack[0] if stack else None
