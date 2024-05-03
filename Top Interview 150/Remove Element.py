class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer to keep track of non-val elements
        k = 0
        # Iterate through the array
        for i in range(len(nums)):
            # If the current element is not equal to val
            if nums[i] != val:
                # Move this element to the beginning of the array
                nums[k] = nums[i]
                # Increment the pointer
                k += 1        
        # Return the number of elements not equal to val
        return k
