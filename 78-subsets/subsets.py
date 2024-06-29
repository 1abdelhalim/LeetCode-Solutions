class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  
        for num in nums:
            new = [curr + [num] for curr in result]
            result.extend(new)
        return result
