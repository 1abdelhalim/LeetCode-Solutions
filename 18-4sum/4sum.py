class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = []
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                left, right = j+1, n-1

                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]

                    if summ == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1 
                        
                        left += 1 
                        right -= 1 

                    elif summ < target:
                        left += 1 
                    else:
                        right -= 1 

        return quadruplets
