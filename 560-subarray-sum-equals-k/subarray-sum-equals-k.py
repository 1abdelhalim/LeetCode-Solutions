class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        curr_sum = 0
        prefix_sum_count = {0: 1}  
        
        for num in nums:
            curr_sum += num  
           
            if (curr_sum - k) in prefix_sum_count:
                count += prefix_sum_count[curr_sum - k]
            
            if curr_sum in prefix_sum_count:
                prefix_sum_count[curr_sum] += 1
            else:
                prefix_sum_count[curr_sum] = 1
        
        return count
