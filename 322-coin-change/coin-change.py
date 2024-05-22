class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(curr_amount, memo):
            if curr_amount < 0:
                return float('inf')
            if curr_amount == 0:
                return 0
            if curr_amount in memo:
                return memo[curr_amount]

            memo[curr_amount] = min(dp(curr_amount - coin, memo) + 1 for coin in coins)
            return memo[curr_amount]

        memo = {}
        result = dp(amount, memo)
        return result if result != float('inf') else -1


          
        