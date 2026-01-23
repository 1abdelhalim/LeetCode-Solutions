class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        n = len(points)

        for i in range(1, n):
            dx = abs(points[i][0] - points[i-1][0])
            dy = abs(points[i][1] - points[i-1][1])
            diagonal_moves = min(dx, dy)
            rem = abs(dx-dy)
            answer += diagonal_moves 
            answer += rem 

        return answer