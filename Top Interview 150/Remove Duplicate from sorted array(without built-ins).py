class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize pointer for the position of the next valid element
        next_valid = 2
        
        # Start iterating from the third element
        for i in range(2, len(nums)):
            # If the current element is different from the two elements before it
            if nums[i] != nums[next_valid - 1] or nums[i] != nums[next_valid - 2]:
                # Place the current element at the position of the next valid element
                nums[next_valid] = nums[i]
                # Move the pointer for the next valid element
                next_valid += 1
        
        return next_valid
            
