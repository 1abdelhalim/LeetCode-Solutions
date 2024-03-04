class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1 
        
        elif target > sum(nums):
            return 0
        
        n = len(nums)
        if target == sum(nums):
            return n
        
        ans = float('inf') 
        curr_sum = 0
        left = 0
        
        for right, num in enumerate(nums):
            curr_sum += num
            
            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
                
        return ans if ans != float('inf') else 0
