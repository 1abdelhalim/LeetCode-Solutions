class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, sum_xor):
            if i == len(nums):
                return sum_xor

            return dfs(i+1, sum_xor ^ nums[i]) + dfs(i + 1, sum_xor)

        return dfs(0, 0)