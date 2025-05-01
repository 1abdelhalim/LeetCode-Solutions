class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y 
        return bin(xor)[2:].count('1')