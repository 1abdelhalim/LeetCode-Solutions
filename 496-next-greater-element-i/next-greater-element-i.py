class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for num in nums1:
            idx = nums2.index(num)  
            next = -1
            for j in range(idx + 1, len(nums2)): 
                if nums2[j] > num:
                    next = nums2[j]
                    break
            ans.append(next)
        return ans

