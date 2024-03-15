class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low, high = 1, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            count = sum(1 for num in nums if num <= mid)

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low
