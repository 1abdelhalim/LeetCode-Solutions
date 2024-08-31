class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0 

        for i in range(n):
            curr_ele = start + 2 * i 
            result ^= curr_ele 

        return result 