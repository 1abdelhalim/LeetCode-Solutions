class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            idx_max = gifts.index(max(gifts))
            gifts[idx_max] = int(gifts[idx_max] ** 0.5)

        return sum(gifts)
