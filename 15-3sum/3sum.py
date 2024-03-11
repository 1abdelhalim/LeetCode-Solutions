class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n = len(nums)
        triplets = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue # skip duplicates

            left, right = i+1, n-1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ > 0:
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1 
        return triplets


        