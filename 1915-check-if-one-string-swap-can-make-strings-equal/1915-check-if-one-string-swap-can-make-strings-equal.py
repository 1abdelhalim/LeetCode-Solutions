from collections import Counter

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter(s2)

        if counter1 == counter2:
            n = len(s1)
            c = 0
            for i in range(n):
                if s1[i] != s2[i]:
                    c += 1 
                if c > 2:
                    break 

            if c == 0 or c == 2:
                return True 

        return False 
            
            