class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0

        for i in range(n):
            total_subs = (i + 1) * (n - i)
            odd_subs = (total_subs + 1) // 2
            result += arr[i] * odd_subs

        return result