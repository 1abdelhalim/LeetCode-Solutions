class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rem_map = {0: 1}  
        curr_sum = 0
        ans = 0

        for num in nums:
            curr_sum += num
            rem = curr_sum % k

            if rem < 0:
                rem += k

            if rem in rem_map:
                ans += rem_map[rem]
                rem_map[rem] += 1
            else:
                rem_map[rem] = 1

        return ans
