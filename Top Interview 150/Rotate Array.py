class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        
        # Reverse the entire array
        nums.reverse()

        # Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
        
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        
        
