class Solution:
    def finalString(self, s: str) -> str:
        n = len(s)
        ans = ""

        for i in range(n):

            if s[i] == "i":
                ans = ans[::-1]
            else:
                ans += s[i]

        return ans
