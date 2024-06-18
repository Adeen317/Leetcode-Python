#15. Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, n - 1
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                if current_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while k < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif current_sum < 0:
                    j += 1
                else:
                    k -= 1
        
        return result
