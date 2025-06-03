class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in nums:
            temp = [curr + [i] for curr in result]
            result.extend(temp)

        return result 