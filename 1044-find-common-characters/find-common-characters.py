from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])

        for word in words[1:]:
            word_count = Counter(word)
            for char in common_count.keys():
                if char in word_count:
                    common_count[char] = min(common_count[char], word_count[char])
                else:
                    common_count[char] = 0


        result = []
        for char, count in common_count.items():
            result.extend([char] * count)

        return result
