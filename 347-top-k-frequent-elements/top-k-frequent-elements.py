from collections import Counter 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq_heap = [(-freq, num) for num, freq in counter.items()]
       
        top_freq = heapq.nsmallest(k, freq_heap)
        
        return [num for freq, num in top_freq]
