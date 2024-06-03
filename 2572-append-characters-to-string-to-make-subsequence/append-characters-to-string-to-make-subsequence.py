class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t == s:
            return 0 
        curr = 0
        count = len(t)
        i = 0 
        while i < len(s) and curr < count:
            if s[i] == t[curr]:
                count -= 1 
                curr += 1 

            i += 1
        return count 
