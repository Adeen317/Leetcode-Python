class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operation = 0
        for i in range(len(nums)):
            reminder = nums[i] % 3
            if reminder == 1:
                operation += 1
            elif reminder == 2:
                operation += 1
        return operation
            
