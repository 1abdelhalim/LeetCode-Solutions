class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # suppose we have a var answer 
        # we can loop through the array and apply the rule 
        # check every time we have nums[i] if satisfy or not 
        # return the final answer 

        ans = float('inf')
        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                ans = min(ans, abs(i-start))


        return ans