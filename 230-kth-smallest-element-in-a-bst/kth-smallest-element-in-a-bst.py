# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        if not root:
            return None 

        queue = deque([root])
        while queue:
            node = queue.popleft()
            result.append(node.val)

            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        result.sort()

        return result[k-1] 
        