class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        min_product = max_product = ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
        
            ans = max(ans, max_product)

        return ans
