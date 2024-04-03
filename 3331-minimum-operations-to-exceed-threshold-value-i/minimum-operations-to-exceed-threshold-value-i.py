class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums) 
        nums.sort()

        for i in range(n):
            if nums[i] >= k:
                break
            count += 1 

        return count