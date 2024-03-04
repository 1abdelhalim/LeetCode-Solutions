class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf') 
        curr_sum = 0
        l = 0
        
        for r, num in enumerate(nums):
            curr_sum += num 
            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
                l += 1 

        return ans if ans != float('inf') else 0 