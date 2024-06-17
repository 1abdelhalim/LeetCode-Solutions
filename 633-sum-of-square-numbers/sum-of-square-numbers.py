import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        square_root = int(math.isqrt(c))
        for a in range(square_root + 1):
            b_squared = c - a ** 2
            if b_squared < 0:
                continue
            b = int(math.isqrt(b_squared))
            if b ** 2 == b_squared:
                return True
        return False
