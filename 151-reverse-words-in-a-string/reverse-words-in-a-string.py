class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_s = ' '.join(reversed(words))
        return reversed_s
