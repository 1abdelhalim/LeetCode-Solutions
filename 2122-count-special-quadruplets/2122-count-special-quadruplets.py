class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
    
        for a in range(n):
            for b in range(a + 1, n):
                for c in range(b + 1, n):
                    for d in range(c+1, n):
                        if nums[d] == nums[a] + nums[b] + nums[c]:
                            count += 1 

                    

    
        
        return count