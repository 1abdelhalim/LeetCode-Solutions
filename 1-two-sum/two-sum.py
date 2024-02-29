class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}

        for i, num in enumerate(nums):
            comp = target - num 
            if comp in comps:
                return [comps[comp], i]
            comps[num] = i