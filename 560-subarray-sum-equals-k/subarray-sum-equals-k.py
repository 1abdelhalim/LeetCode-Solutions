class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sum_count = {0: 1}  
        
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            count += prefix_sum_count.get(diff,0)
            prefix_sum_count[curr_sum] = prefix_sum_count.get(curr_sum, 0 ) +1 

        return count