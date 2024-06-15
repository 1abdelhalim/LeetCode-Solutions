from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        
        min_heap = []
        max_heap = []
        
        for c, p in projects:
            heappush(min_heap, (c, p))
        
        for _ in range(k):
    
            while min_heap and min_heap[0][0] <= w:
                c, p = heappop(min_heap)
                heappush(max_heap, -p)
            
            if not max_heap:
                break
            
            w += -heappop(max_heap)
        
        return w