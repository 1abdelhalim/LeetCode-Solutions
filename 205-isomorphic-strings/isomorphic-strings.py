class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        len_set_s = len(set(s))
        len_set_t = len(set(t))
        if len_set_s != len_set_t:
            return False  
        zipped_set = set(zip(s, t))
        return len(zipped_set) == len_set_s  == len_set_t
