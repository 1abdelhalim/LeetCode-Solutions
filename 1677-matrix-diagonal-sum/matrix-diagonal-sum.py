class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0 
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if i == j:
                    ans += mat[i][j]
                elif i + j == n-1:
                    ans += mat[i][j]

        return ans
