class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        set_s = set(s)
        set_t = set(t)
        if len(set_s) != len(set_t):
            return False  
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len(set_s) == len(set_t)
