class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices[:]
        n = len(prices)
        stack = []

        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]

            stack.append(i)

        return result 