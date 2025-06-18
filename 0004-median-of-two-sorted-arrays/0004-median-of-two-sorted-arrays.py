class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1+nums2
        merge.sort()

        n = len(merge)

        if n%2 != 0:
            return merge[n//2]
        else:
            return (merge[n//2] + merge[n//2 - 1]) / 2
