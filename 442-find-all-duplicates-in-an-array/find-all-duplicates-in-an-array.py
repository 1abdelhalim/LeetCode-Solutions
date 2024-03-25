class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        duplicates = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1 
        
        for key, val in freq.items():
            if val > 1:
                duplicates.append(key)
        
        return duplicates
