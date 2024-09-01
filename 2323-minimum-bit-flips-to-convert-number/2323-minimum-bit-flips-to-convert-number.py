class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_op = start ^ goal 

        return bin(xor_op).count('1')