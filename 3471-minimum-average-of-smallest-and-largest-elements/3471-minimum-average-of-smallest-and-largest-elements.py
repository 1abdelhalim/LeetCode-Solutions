class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        x = float('inf')
        nums.sort()
        for i in range(len(nums) // 2):
            x = min(x, (nums[i] + nums[len(nums) - 1 - i]) / 2.0)
        return x
