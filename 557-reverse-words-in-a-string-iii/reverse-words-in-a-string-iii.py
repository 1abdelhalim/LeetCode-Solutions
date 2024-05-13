class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        n = len(words)

        for i in range(n):
            words[i] = words[i][::-1]

        return " ".join(words)