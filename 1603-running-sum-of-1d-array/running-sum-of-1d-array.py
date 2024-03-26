class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [0]
        n = len(nums)

        for i in range(n):
            temp =  nums[i] + prefix[i]
            prefix.append(temp)

        return prefix[1:]