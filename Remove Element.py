class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize a pointer j to track the valid elements without 'val'
        j = 0
        
        # Iterate through the nums list
        for i in range(len(nums)):
            # If the current element is not equal to the given 'val'
            if nums[i] != val:
                # Replace the element at position 'j' with the valid element at position 'i'
                nums[j] = nums[i]
                # Increment the pointer 'j' to point to the next valid position
                j += 1
        
        # 'j' represents the length of the modified nums list without the 'val'
        return j
