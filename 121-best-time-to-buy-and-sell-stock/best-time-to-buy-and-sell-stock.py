class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        l = 0  
        max_profit = 0

        for r in range(1, n):  
            if prices[r] > prices[l]:
                curr_profit = prices[r] - prices[l]
                max_profit = max(max_profit, curr_profit)
            else:
                l = r 
        return max_profit
