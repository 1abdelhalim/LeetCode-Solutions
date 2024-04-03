class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = sum(nums)
        dig_sum = 0

        for num in nums:
            while num > 0:
                dig_sum += num % 10
                num //= 10

        return abs(ele_sum - dig_sum)
