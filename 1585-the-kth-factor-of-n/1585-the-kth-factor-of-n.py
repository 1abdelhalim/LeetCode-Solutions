class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        def is_prime(n):
            if n == 1:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        if is_prime(n):
            if k == 1:
                return 1 
            elif k == 2:
                return n
            else:
                return -1 

        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1 
            if count == k:
                return i 
                break

        return -1 



 
