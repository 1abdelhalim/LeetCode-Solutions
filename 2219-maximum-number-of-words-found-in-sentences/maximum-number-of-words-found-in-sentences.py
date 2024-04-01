class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 1

        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))

        return max_words

            