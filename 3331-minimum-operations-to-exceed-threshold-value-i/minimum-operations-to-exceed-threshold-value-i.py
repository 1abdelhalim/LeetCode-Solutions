class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums) 

        for i in range(n):
            if nums[i] < k:
                count += 1 

        return count