class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map = {0: -1}
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            rem = curr_sum % k
            
            if rem in rem_map:
                if i - rem_map[rem] > 1:  
                    return True
            else:
                rem_map[rem] = i
        
        return False
