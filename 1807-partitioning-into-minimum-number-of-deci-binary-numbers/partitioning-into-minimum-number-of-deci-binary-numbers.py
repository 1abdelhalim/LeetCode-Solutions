class Solution:
    def minPartitions(self, n: str) -> int:
        ans = float('-inf')
        for dig in n:
            ans = max(ans, int(dig))

        return ans