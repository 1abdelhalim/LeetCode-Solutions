class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        n = len(nums)
        perms = []
        for i in range(n):
            curr = nums[i]
            rem = nums[:i] + nums[i+1:]
            for perm in self.permute(rem):
                perms.append([curr] + perm)
        
        return perms
