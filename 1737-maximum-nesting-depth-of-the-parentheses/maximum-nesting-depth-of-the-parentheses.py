class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        curr = 0

        for char in s:
            if char == "(":
                curr += 1
                max_depth = max(max_depth, curr)
            elif char == ")":
                curr -= 1

        return max_depth