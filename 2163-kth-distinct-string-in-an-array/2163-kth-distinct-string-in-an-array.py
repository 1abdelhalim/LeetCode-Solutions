class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq = {}

        for ch in arr:
            freq[ch] = freq.get(ch, 0) + 1

        distinct_count = 0
        for ch in arr:
            if freq[ch] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return ch
        
        return ""