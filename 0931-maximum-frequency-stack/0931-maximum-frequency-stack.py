class FreqStack:
    def __init__(self):
        self.max_heap = []
        self.freq = {}
        self.counter = 0      

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0)+1

        heapq.heappush(self.max_heap, (-self.freq[val], -self.counter, val))
        self.counter += 1
        
    def pop(self) -> int:
        temp = heapq.heappop(self.max_heap)
        self.freq[temp[2]]-=1
        return temp[2]

