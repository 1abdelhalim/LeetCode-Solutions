class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False 
        if target in nums:
            found = True

        return nums.index(target) if found else  -1

