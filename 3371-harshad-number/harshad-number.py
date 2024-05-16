class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = sum(int(dig) for dig in str(x))

        if x % sum_digits == 0:
            return sum_digits
        
        return -1 