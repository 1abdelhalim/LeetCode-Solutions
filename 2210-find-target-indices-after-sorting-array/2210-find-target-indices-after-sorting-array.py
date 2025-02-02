class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        n = len(nums)

        result = []
        for i in range(n):
            if nums[i] == target:
                result.append(i)

        return result 