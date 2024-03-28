class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r = 0, 0
        count = 0
        for ch in s:
            if ch == 'R': r += 1
            if ch == 'L': l += 1
            if l == r: count += 1
        return count