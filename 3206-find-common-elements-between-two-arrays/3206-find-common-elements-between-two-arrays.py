class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_nums1 = {}
        freq_nums2 = {}
        i = 0 
        j = 0 

        for num in nums1:
            freq_nums1[num] = freq_nums1.get(num, 0) + 1 


        for num in nums2:
            freq_nums2[num] = freq_nums2.get(num, 0) + 1

     
        for key, val in freq_nums1.items():
            if key in freq_nums2.keys():
                i += val

        for key, val in freq_nums2.items():
            if key in freq_nums1.keys():
                j += val
        return [i, j]

        
