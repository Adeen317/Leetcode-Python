class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numm = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in numm:
                return [numm[comp], i]
            numm[nums[i]] = i

            
