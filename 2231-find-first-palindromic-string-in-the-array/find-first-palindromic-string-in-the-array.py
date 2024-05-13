class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindrome = next(filter(lambda x: x == x[::-1], words), "")
        return palindrome
