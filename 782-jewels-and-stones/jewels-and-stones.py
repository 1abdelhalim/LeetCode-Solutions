class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = {}
        count = 0 

        for ch in stones:
            if ch in freq:
                freq[ch] += 1 
            else:
                freq[ch] = 1 

        for ch in jewels:
            if ch in freq:
                count += freq[ch]

        return count