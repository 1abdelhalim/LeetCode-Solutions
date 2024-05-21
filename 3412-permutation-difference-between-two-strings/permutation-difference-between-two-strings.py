class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_indeces = {}
        t_indeces = {}
        n = len(s)

        for i in range(n):
            s_indeces[s[i]] = i 
            t_indeces[t[i]] = i 
            
        ans = 0 
        for char in s:
            ans += abs(s_indeces[char] - t_indeces[char])

        return ans
            