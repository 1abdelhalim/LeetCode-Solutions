class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1 

        for key, val in freq.items():
            if val == 1:
                return s.index(key) 

        return -1 