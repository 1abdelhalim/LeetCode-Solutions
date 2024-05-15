class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n 

        a = 0 
        b = 1

        for i in range(1, n):
            temp = a 
            a = b 
            b = temp + b 

        return  b 
