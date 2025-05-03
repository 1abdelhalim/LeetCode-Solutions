class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor_op = start ^ goal 
        to_bin = bin(xor_op)[2:]

        result = to_bin.count("1")

        return result