class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        left_sum = 0
        for i in range(n):
            left_sum += nums[i]
            result.append(left_sum)

        right_sum = 0
        for i in range(n - 1, -1, -1):
            right_sum += nums[i]
            result[i] = abs(result[i] - right_sum)

        return result