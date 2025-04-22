class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)

        def backtrack(start, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            if total > target:
                return

            for i in range(start, n):
                curr.append(candidates[i])
                backtrack(i, curr, total + candidates[i])
                curr.pop() 

        backtrack(0, [], 0)
        return result