class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)

        max_area = 0 
        for i in range(n):
            for j in range(1, n):
                for k in range(2, n):
                    area = 0.5*abs(points[i][0] *(points[j][1] - points[k][1]) + points[j][0]*(points[k][1]-points[i][1]) + points[k][0]*(points[i][1]-points[j][1]))
                    max_area = max(max_area, area)


        return max_area