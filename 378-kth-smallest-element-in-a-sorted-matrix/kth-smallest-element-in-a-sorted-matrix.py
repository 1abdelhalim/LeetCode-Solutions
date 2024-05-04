class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for m in matrix:
            for num in m:
                arr.append(num)
                
        arr.sort()
        return arr[k-1]