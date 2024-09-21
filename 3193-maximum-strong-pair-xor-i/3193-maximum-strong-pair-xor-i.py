class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0  

        n = len(nums)
        for i in range(n):
            for j in range(i+1, n): 
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    max_xor = max(max_xor, nums[i] ^ nums[j])

        return max_xor
