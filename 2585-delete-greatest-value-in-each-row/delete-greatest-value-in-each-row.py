class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0 

        while any(grid):
            max_val = float('-inf')
            n = len(grid)

            for i in range(n):
                if grid[i]:
                    curr_max = max(grid[i])
                    grid[i].remove(curr_max)
                    max_val = max(max_val, curr_max)

            ans += max_val 

        return ans
