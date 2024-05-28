class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n

        balls = 0
        ops = 0
        for i in range(n):
            ans[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        balls = 0
        ops = 0
        for i in range(n-1, -1, -1):
            ans[i] += ops
            if boxes[i] == '1':
                balls += 1
            ops += balls

        return ans