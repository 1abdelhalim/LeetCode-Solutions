class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for num in nums:
            ans |= num
        
        return ans * (2 ** (n - 1))
