class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Iterate through the list backwards
        for num in nums[::-1]:
            # If the count of the current element is greater than 2, remove excess occurrences
            while nums.count(num) > 2:
                nums.remove(num)
        
        # Return the length of the modified list
        return len(nums)
            
