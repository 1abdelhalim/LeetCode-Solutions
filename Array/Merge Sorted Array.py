class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        i = m - 1  # Pointer for nums1
        j = n - 1  # Pointer for nums2
        k = m + n - 1  # Pointer for the merged array
        
        # Loop until we've merged all elements from nums2 into nums1
        while j >= 0:
            # If there are elements remaining in nums1 and nums1's current element is greater
            # than the current element in nums2, place nums1's element at the end of the merged array
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                # If nums1's current element is smaller than or equal to the current element in nums2,
                # place nums2's current element at the end of the merged array
                nums1[k] = nums2[j]
                j -= 1
            # Move the pointer for the merged array to the previous position
            k -= 1
