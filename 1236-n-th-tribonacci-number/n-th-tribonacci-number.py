class Solution:
    def tribonacci(self, n: int) -> int:
        def trib_memo(n, memo={}):  # Added colon here
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            if n == 2:
                return 1 

            memo[n] = trib_memo(n-1) + trib_memo(n-2) + trib_memo(n-3)

            return memo[n]

        return trib_memo(n) 
