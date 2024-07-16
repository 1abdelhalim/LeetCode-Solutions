class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        n = len(nums)
        expexted_sum = n * (n+1) // 2 
        curr_sum = sum(nums)

        return expexted_sum - curr_sum