class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        n = len(nums)

        for i in range(0, n, 2):
            temp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = temp 

        return nums

       