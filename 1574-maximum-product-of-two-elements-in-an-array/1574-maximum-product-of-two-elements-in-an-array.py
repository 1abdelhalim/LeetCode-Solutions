class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]
        b = nums[-2]

        return (a-1) * (b-1)