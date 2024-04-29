class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0 
        indeces = {0:0}

        for i, num in enumerate(nums,1):
            count += 1 if num  else -1 
            if count in indeces:
                max_length = max(max_length, i - indeces[count])
            else:
                indeces[count] = i 
        return max_length
