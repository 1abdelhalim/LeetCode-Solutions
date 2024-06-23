from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        ans = 0 

        while queue:
            ans = 0  
            for _ in range(len(queue)):
                node = queue.popleft()

                if not node.left and not node.right:
                    ans += node.val 

                if node.left:
                    queue.append(node.left)  
                if node.right:
                    queue.append(node.right) 

        return ans
