class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n == 1:
            return 1 
        elif n == 2:
            return 2  
        elif n in memo:
            return memo[n]
        else: 
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return memo[n]