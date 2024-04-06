class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s 
        else:
            i = 1
            while i < len(s):
                curr = s[i]
                prev = s[i-1]
                if curr.lower() == prev.lower() and curr != prev:
                    s = s.replace(prev+curr, "")
                    i = 0  
                i += 1 
            return s 
