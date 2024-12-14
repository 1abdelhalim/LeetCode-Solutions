class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums = [2,7,11,15], target = 9 
        # hash = {2:0 , 7:1, 11:2, 15:3}
        hash_map = {}
        n = len(nums)
        for i in range(n):
            hash_map[nums[i]] = i 

        # target - nums[j] 
        for j in range(n):
            # 2 
            temp = target - nums[j] # 7

            if temp in hash_map and hash_map[temp] != j:
                # not the same idx 
                return [j, hash_map[temp]]