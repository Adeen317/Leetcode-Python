class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a_i = nums1 + nums2
        a_i.sort()
        n = len(a_i)
        if n % 2 == 0:
            return (a_i[n // 2 - 1] + a_i[n // 2]) / 2.0
        else:
            return a_i[n // 2]

        
