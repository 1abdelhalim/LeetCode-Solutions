class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices
        n = len(prices)

        for i in range(n-1):
            for j in range(i+1, n):
                if prices[i] >= prices[j]:
                    result[i] = (prices[i] - prices[j])
                    break 

        return result

                