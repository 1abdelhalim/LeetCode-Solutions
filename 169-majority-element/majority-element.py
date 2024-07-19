from collections import Counter 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_freq = Counter(nums)
        n = len(nums)

        for key, value in hash_freq.items():
            if value > (n / 2 ):
                return key 
                