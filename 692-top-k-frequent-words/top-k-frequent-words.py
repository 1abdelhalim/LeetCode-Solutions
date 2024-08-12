class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        top_k = [key for key, _ in sorted(counter.items(),
                 key=lambda x: (-x[1], x[0]))[:k]]

        return top_k