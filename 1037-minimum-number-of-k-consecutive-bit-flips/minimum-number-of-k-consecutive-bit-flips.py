class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        curr = 0  
        total = 0  

        for i in range(len(nums)):
            
            if i >= k and nums[i - k] == 2:
                curr -= 1

            if (curr % 2) == nums[i]:
               
                if i + k > len(nums):
                    return -1

                nums[i] = 2
                curr += 1
                total += 1

        return total