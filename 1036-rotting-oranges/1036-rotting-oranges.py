class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid) 
        n = len(grid[0]) 
        result = 0

        while True:
            matrix = [row[:] for row in grid]
            rotted = False 

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            k, l = i + x, j + y
                            if 0 <= k < m and 0 <= l < n and grid[k][l] == 1:
                                matrix[k][l] = 2
                                rotted = True

            if not rotted:
                break

            grid = matrix
            result += 1

        for row in grid:
            if 1 in row:
                return -1

        return result
