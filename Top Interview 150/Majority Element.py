class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        # The majority element will always be at the middle index
        majority = len(nums) // 2
        
        # Return the element at the middle index
        return nums[majority]
        
