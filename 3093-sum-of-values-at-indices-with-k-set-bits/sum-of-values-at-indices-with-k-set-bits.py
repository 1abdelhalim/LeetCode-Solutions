class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            if bin(i).count("1") == k:
                result += nums[i]


        return result