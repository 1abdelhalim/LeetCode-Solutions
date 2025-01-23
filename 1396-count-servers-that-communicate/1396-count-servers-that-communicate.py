class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(col) for col in zip(*grid)]
        
        result = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    result += 1
        
        return result