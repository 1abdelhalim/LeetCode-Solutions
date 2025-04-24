from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if total > target:
                return

            prev = -1  
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return result
