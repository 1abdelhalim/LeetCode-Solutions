class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        
        dp = []
        for row in triangle:
            dp.append([0] * len(row))
            
        for c in range(len(triangle[-1])):
            dp[n - 1][c] = triangle[n - 1][c]
            
        for r in range(n - 2, -1, -1):
            for c in range(len(triangle[r])):
                
                left_child = dp[r + 1][c]
                right_child = dp[r + 1][c + 1]
                
                best_path_below = min(left_child, right_child)
                dp[r][c] = triangle[r][c] + best_path_below
                
        return dp[0][0]