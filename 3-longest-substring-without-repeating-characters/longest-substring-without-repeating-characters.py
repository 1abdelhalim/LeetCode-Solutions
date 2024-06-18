class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        i = 0
        longest = 0

        for j in range(n):
            for k in range(i, j):
                if s[k] == s[j]:
                    i = k + 1
                    break
            longest = max(longest, j - i + 1)

        return longest
