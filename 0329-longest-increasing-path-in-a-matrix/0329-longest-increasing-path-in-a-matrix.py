

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[-1] * n for _ in range(m)]
        max_path = 0

        for i in range(m):
            for j in range(n):
                max_path = max(max_path, solve(dp, i, j, matrix, m, n))

        return max_path


def solve(dp, i, j, matrix, m, n):
    if dp[i][j] != -1:
        return dp[i][j]
    
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    max_len = 1  

    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
            max_len = max(max_len, 1 + solve(dp, ni, nj, matrix, m, n))

    dp[i][j] = max_len
    return dp[i][j]