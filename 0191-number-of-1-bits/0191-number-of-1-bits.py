class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = str(bin(n)[2:])
        ones = binary.count("1")

        return ones
