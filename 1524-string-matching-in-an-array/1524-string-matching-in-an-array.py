class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = ' '.join(words)
        result = []
        for w in words:
            if s.count(w) > 1:
                result.append(w)
        return result