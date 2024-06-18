class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        i = 0
        longest = 0
        ch_idx = {}

        for j in range(n):
            if s[j] in ch_idx and ch_idx[s[j]] >= i:
                i = ch_idx[s[j]] + 1

            ch_idx[s[j]] = j
            longest = max(longest, j - i + 1)

        return longest
