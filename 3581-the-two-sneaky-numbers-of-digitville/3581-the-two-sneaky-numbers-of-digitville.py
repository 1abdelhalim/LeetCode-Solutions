class Solution:
    def getSneakyNumbers(self, nums):
        from collections import Counter
        counter = Counter(nums)
        result = []

        for key in counter:
            if counter[key] == 2:
                result.append(key)

        return result     