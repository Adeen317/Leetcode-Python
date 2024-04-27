class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2
    
        # Sort the entire array
        nums1.sort()

        merge(nums1, m, nums2, n)
            
            
