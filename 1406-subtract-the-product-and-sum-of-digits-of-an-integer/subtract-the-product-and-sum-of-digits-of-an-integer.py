class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1 
        to_str = str(n)
        for num in to_str:
            prod *= int(num)
        
        summ = 0
        for num in to_str:
            summ += int(num)

        diff = prod - summ 
        return diff       