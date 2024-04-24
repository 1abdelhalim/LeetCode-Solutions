class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    
        return sorted_nums