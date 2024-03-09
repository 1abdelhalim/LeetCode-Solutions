class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  
        n = len(nums)
        ans = float('inf')  

        for i in range(n):
            left, right = i + 1, n - 1  
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                
                if abs(curr - target) < abs(ans - target):
                    ans = curr 
                    
                if curr < target:
                    left += 1  
                elif curr > target:
                    right -= 1  
                else:
                    return target  

        return ans  
