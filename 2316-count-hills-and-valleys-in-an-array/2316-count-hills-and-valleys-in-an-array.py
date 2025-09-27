class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # start from index 1 
        # we can iterate from 1 to n-1
        # use 2 while loops 
        # one for right and the other for left 

        n = len(nums)

        count = 0
        for i in range(1, n-1):
            if nums[i] == nums[i-1]:
                continue 
            r = i + 1 
            while r < n and nums[r] == nums[i]:
                
                r += 1 

            l = i - 1 
            while l >= 0 and nums[l] == nums[i]:
                l -= 1

            if l >= 0 and r < n:
                if nums[i] > nums[r] and nums[i] > nums[l]:
                    count +=1 
                elif nums[i] < nums[r] and nums[i] < nums[l]:
                    count +=1 


        return count  


