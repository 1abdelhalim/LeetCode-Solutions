class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = 1 
        while True:
            if num % 2 == 0 and num % n == 0:
                return num 
            num += 1 