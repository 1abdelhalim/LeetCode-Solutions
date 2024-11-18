class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ascii_s = sum(ord(ch) for ch in s )
        ascii_t = sum(ord(ch) for ch in t)

        return chr((ascii_t - ascii_s))