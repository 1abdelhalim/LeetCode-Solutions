class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # min heap 
        self.min_heap = nums

        heapq.heapify(self.min_heap)
        #keep the k largest nums in the heap
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]