class Solution:
    def maxDistinct(self, s: str) -> int:
        chars_freq = {}
        for ch in s:
            chars_freq[ch] = chars_freq.get(ch, 0) + 1

        return len(chars_freq.keys())

        

