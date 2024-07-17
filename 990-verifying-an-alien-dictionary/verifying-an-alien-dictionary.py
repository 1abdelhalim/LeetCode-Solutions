class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        order_index = {char: idx for idx, char in enumerate(order)}
        
        def is_sorted(word1, word2):
            len1, len2 = len(word1), len(word2)
            for i in range(min(len1, len2)):
                if word1[i] != word2[i]:
                    return order_index[word1[i]] < order_index[word2[i]]
            return len1 <= len2

        for i in range(len(words) - 1):
            if not is_sorted(words[i], words[i + 1]):
                return False

        return True
