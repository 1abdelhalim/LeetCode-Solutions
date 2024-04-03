class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum = sum(nums)
        digits = ""
        dig_sum = 0

        for num in nums:
            digits += str(num)

        for dig in digits:
            dig_sum += int(dig)

        return abs(ele_sum - dig_sum)