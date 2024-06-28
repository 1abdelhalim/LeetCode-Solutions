class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        freq = [0] * n
        for road in roads:
            for num in road:
                freq[num] += 1

        sorted_freq = sorted(range(n), key=lambda x: freq[x])

        imp = [0] * n
        for i in range(n):
            imp[sorted_freq[i]] = i + 1

        max_total = 0
        for i, j in roads:
            max_total += imp[i] + imp[j]

        return max_total
