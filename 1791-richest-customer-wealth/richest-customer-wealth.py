class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for account in accounts:
            total = sum(account)
            if ans < total:
                ans = total 

        return ans