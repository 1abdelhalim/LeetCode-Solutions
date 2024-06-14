class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
     
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                inc = nums[i - 1] - nums[i] + 1
                nums[i] += inc
                count += inc
        
        return count