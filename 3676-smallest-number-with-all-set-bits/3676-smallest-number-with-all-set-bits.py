class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = bin(n)[2:]
        def all_ones(n):
            return n > 0 and (n & (n + 1)) == 0

        while all_ones(n) != True:
            n += 1 
            all_ones(n)

        return n 