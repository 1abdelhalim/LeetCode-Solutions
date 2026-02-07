class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n 
        def move(i, k, n):
            return (i + k) % n

        for i in range(n):
            if nums[i] == 0:
                result[i] = 0 
            else:
                result[i] = nums[move(i, nums[i], n)]

        return result 


