class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        high_bit = 1
        
        for i in range(1, n + 1):
            if i == high_bit * 2:
                high_bit = high_bit * 2
            ans[i] = 1 + ans[i - high_bit]
        
        return ans
