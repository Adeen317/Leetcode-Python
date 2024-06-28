class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        sum1=0
        total_sum = n * (n + 1) // 2
        for i in range(n):
            sum1 += nums[i]
        return total_sum - sum1
