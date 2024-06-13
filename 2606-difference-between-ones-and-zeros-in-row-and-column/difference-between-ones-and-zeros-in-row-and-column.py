class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        
        row_ones = [0] * n
        row_zeros = [0] * n
        col_ones = [0] * m
        col_zeros = [0] * m
        
        for i in range(n):
            row_ones[i] = sum(grid[i])
            row_zeros[i] = m - row_ones[i]
        
        for j in range(m):
            col_ones[j] = sum(grid[i][j] for i in range(n))
            col_zeros[j] = n - col_ones[j]
        
        diff = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                diff[i][j] = row_ones[i] + col_ones[j] - row_zeros[i] - col_zeros[j]
        
        return diff
