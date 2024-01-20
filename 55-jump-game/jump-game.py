class Solution:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0 
        l = len(nums)
        
        for i in range(l):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])

            if max_reach >= l - 1:
                return True
        return True

        




        