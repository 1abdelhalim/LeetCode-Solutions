class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= multiplier

        return nums