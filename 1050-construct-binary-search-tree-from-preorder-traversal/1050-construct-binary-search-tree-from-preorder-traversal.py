# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)  
        curr = root

        for i in range(1, len(preorder)):
            temp = TreeNode(preorder[i])  

            if temp.val < stack[-1].val: 
                curr.left = temp
                stack.append(temp)
                curr = temp  

            else:  
                while stack and stack[-1].val < temp.val:
                    curr = stack.pop()  

                curr.right = temp
                stack.append(temp)  
                curr = temp  

        return root