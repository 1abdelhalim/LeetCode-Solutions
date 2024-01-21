class Solution:
    def rob(self, nums: list[int]) -> int:
        way1 = 0 
        way2 = 0

        for n in nums:
            temp = max(n + way1, way2)
            way1 = way2
            way2 = temp 

        return way2