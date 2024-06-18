class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        
        for j in range(1, n):
            curr = prices[j] - prices[j - 1]
            if curr > 0:
                max_profit += curr

        return max_profit
