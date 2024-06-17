class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        repeated = 0
        missing = 1
        n = len(grid)

        ans = []

        for i in range(n):
            for j in range(n):
                curr = grid[i][j]
                if curr in seen:
                    repeated = curr
                else:
                    seen.add(curr)
        
        while missing in seen:
            missing += 1

        ans.append(repeated)
        ans.append(missing)
        return ans
