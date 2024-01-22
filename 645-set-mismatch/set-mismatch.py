class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq[n] == 2:
                res.append(n)

        length = len(nums)
        for i in range(1, length+1):
            if i not in freq:
                res.append(i)
        
        return res