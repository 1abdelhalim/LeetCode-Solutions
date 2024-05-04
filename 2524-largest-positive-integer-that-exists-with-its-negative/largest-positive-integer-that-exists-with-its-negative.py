class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        maxx = float('-inf')
        for num in nums:
            if -num in s:
                maxx = max(maxx, num)
        return maxx if maxx != float('-inf') else -1
