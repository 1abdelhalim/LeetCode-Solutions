class Solution:
    def sumBase(self, n: int, k: int) -> int:
        digits = []
        while n > 0:
            remainder = n % k  
            digits.append(remainder)
            n = n // k  

        return sum(digits)