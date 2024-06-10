class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        n = len(heights)
        count = 0 

        for i in range(n):
            if heights[i] != sorted_heights[i]:
                count += 1

        return count 