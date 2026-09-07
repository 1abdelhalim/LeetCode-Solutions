class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        
        for i in range(32):
            bit_sum = 0
            
            for num in nums:
                bit_sum += (num >> i) & 1

            if bit_sum % 3 != 0:
                result |= (1 << i)
                
        if result >= 2**31:
            result -= 2**32
            
        return result