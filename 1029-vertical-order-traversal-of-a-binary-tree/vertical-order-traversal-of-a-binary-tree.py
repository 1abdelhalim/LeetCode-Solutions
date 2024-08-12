# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        column_table = defaultdict(list)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            
            if node is not None:
                column_table[col].append((row, node.val))
                
                if node.left:
                    queue.append((node.left, row + 1, col - 1))
                if node.right:
                    queue.append((node.right, row + 1, col + 1))
        
        sorted_cols = sorted(column_table.keys())
        result = []
        
        for col in sorted_cols:
            sorted_nodes = sorted(column_table[col], key=lambda x: (x[0], x[1]))
            result.append([val for row, val in sorted_nodes])
        
        return result
