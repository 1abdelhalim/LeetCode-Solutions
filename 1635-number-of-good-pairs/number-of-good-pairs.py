class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        count = 0

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1 
        
        for val in freq.values():
            if val > 1:
                count += val * (val-1) // 2 
        
        return count
