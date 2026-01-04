class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            res = []
            d = 1
            while d * d <= n:
                if n % d == 0:
                    res.append(d)
                    if d != n // d:
                        res.append(n // d)
                    
                d += 1
            return sorted(res)

        result = []
        for num in nums:
            temp = divisors(num)
            if  len(temp)== 4:
                result.append(sum(temp))

        return sum(result)


