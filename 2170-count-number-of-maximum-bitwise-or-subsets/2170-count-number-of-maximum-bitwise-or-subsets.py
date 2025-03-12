from itertools import combinations

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or = 0
        count = 0

        for num in nums:
            max_or |= num 

        
        for r in range(1, n + 1):
            for subset in combinations(nums, r):
                subset_or = 0
                for num in subset:
                    subset_or |= num  
                
                if subset_or == max_or:
                    count += 1

        return count
