from collections import Counter
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        
        card_count = Counter(nums)
        unique_cards = sorted(card_count.keys())
        
        for card in unique_cards:
            if card_count[card] > 0:
                start_count = card_count[card]
                for i in range(card, card + k):
                    if card_count[i] < start_count:
                        return False
                    card_count[i] -= start_count
        
        return True
