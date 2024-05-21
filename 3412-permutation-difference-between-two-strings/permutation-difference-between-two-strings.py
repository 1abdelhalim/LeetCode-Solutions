class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        n = len(s)
        
        for i in range(n):
            ans += abs(i - t.index(s[i]))

        return ans
