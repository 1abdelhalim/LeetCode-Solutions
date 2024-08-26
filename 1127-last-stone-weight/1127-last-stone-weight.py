class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            diff = stones[0] - stones[1]
            stones.pop(1)
            stones.pop(0)
            
            if diff > 0:
                stones.append(diff)

        return stones[0] if len(stones) > 0 else 0 