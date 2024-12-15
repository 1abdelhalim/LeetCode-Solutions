class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s) 
        if len(goal) != n:
            return False 

        for i in range(n):
            temp = s[0]
            s = s[1:] + temp

            if s == goal:
                return True 

        return False 