class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        min_ops = [0] * n 


        for i in range(n):
            for j in range(n):
                if boxes[j] == "1":
                    min_ops[i] += abs(i-j)

        return min_ops