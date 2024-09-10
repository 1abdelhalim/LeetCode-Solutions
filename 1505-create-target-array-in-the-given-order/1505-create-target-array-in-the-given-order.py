class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for (num,i) in zip(nums,index):
            result.insert(i,num)
        return result