class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the arraay 
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            l, r  = i+1, n-1

            while l < r:
                summ = nums[i] + nums[l] + nums[r]

                if summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1
                else:
                    result.append([nums[i],nums[l], nums[r]])
                    l += 1 
                    while l < r and nums[l] == nums[l-1]:
                        l += 1 

        return result 