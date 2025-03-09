class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hash_map = {}

        for key, val in nums1:
            hash_map[key] = hash_map.get(key, 0) + val  

        for key, val in nums2:
            hash_map[key] = hash_map.get(key, 0) + val  

        result = []
        for key, val in hash_map.items():
            result.append([key, val])

        return sorted(result)  
