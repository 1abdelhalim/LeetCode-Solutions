class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_ops = 0 
        n = len(nums)

        for num in nums:
            if num % 3 == 0:
                continue
            elif (num-1) % 3 == 0 or (num+1) %3 ==0:
                min_ops +=1 
            else:
                min_ops += 2 

        return min_ops
                