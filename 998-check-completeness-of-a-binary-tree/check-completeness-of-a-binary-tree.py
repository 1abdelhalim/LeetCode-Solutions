# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        found_none = False

        while queue:
            node = queue.popleft()
            if node:
                if found_none:
                    return False

                queue.append(node.left) 
                queue.append(node.right)

            else:
                found_none = True 

        return True 