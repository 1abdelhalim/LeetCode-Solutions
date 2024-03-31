class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points)
        max_ver_area = 0 

        for i in range(1, len(points)):
            max_ver_area = max(max_ver_area, points[i][0] - points[i-1][0])

        return max_ver_area