class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        i = 0 

        # [0,0,1,1,1,2,2,3,3,4]
        for j in range(1, length):
            if nums[i] != nums[j]:
                i += 1 
                nums[i] = nums[j] 


        k = i + 1 
        return k 
        

            


     
