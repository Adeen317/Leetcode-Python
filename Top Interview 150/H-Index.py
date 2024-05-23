class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=0
        citations.sort()
        n=len(citations)
        for i in range(n):
            if citations[i] >= n-i:
                h = n - i
                break
        return h
