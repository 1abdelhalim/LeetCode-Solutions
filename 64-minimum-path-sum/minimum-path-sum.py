class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, cols):
            dp[0][i] = grid[0][i] + dp[0][i-1]

        for j in range(1, rows):
            dp[j][0] = grid[j][0] + dp[j-1][0]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[rows-1][cols-1]