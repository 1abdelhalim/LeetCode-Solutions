class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
    
        max_xor = 0
    
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    xor_value = nums[i] ^ nums[j]
                    max_xor = max(max_xor, xor_value)
    
        return max_xor
