class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []

        n = len(words)

        for i in range(n):
            for j in range(n):
                if words[i] in words[j] and words[i] != words[j]:
                    result.append(words[i])

        return list(set(result))