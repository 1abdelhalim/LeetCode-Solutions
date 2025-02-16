class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = []
        n = len(nums)

        for i in range(n):
            curr = nums[i]
            rem = nums[:i] + nums[i+1:]

            for perm in self.permuteUnique(rem):
                perms.append([curr] + perm)


        return list(map(list, set(tuple(sublist) for sublist in perms)))

