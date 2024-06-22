class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        odd_count = 0
        left = 0
        result = 0

        for right in range(n):
            if nums[right] % 2 == 1:
                odd_count += 1

            while odd_count > k:
                if nums[left] % 2 == 1:
                    odd_count -= 1
                left += 1

            if odd_count == k:
                temp = left
                while odd_count == k:
                    result += 1
                    if nums[temp] % 2 == 1:
                        odd_count -= 1
                    temp += 1
                while temp > left:
                    if nums[temp - 1] % 2 == 1:
                        odd_count += 1
                    temp -= 1

        return result
