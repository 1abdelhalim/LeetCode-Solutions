class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        min_ops = [0] * n

        # left to right 
        balls = 0 
        ops = 0 

        for i in range(n):
            min_ops[i]+= ops 
            if boxes[i] == "1":
                balls+=1 

            ops += balls 

        # right to left 
        balls = 0 
        ops = 0 
        for i in range(n-1, -1, -1):
            min_ops[i] += ops
            if boxes[i] =="1":
                balls += 1 

            ops += balls 


        return min_ops