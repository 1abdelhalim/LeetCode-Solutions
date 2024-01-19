class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows - 2, -1, -1):
            for j in range(cols):
                matrix[i][j] += min(matrix[i + 1][max(0, j - 1):min(cols, j + 2)])
            
        return min(matrix[0])