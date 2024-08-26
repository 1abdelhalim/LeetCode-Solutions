class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num)[2:])
        return (2 ** n) - num - 1 