from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_freq[:k]]
