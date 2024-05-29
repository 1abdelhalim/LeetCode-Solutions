class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = {}
        for edge in edges:
            for v in edge:
                freq[v] = freq.get(v, 0) + 1

        for v, count in freq.items():
            if count == len(edges):
                return v