class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0 
        for num in nums:
            for dig in str(num):
                if int(dig) == digit:
                    count += 1 


        return count 