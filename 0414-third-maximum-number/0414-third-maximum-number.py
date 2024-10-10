class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        
        if len(nums_set) < 3:
            return max(nums_set)

        else:
            sorted_set = sorted(nums_set, reverse=True)
            return sorted_set[2]
