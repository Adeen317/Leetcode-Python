class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []


        for start in range(len(nums)):
            current_sum = 0
            for end in range(start, len(nums)):
                current_sum += nums[end]
                subarray_sums.append(current_sum)

        subarray_sums.sort()
        result_sum = sum(subarray_sums[left - 1:right])

        return result_sum % MOD
