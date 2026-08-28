class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0 
        for num in nums:
            while num:
                temp = num % 10 
                num //= 10
                if temp == digit:
                    count += 1 


        return count 