class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        sorted_nums = sorted(nums)
        n = len(nums)
        
        min_diff = float('inf')
        
        for i in range(n - k + 1):
            diff = sorted_nums[i + k - 1] - sorted_nums[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
