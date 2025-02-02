class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        if n == 1:
            return True 

        def check_parity(num):
            if num % 2 == 0:
                return 1
            else:
                return 0 
        
        i = 0 
        j = 1 

        while j < n:
            if check_parity(nums[i]) == check_parity(nums[j]):
                return False 

            i += 1 
            j += 1 

        return True   
