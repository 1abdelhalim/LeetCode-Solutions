from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to handle duplicates
        result = [[]]
        
        for num in nums:
            new = [curr + [num] for curr in result]
            result.extend(new)
 
        unique_result = list(map(list, set(map(tuple, result))))
        
        return unique_result
