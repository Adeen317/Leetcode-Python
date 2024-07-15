class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = []
        for i in range(numRows):
            b = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    b.append(1)  # The first and last elements in each row are 1
                else:
                    b.append(a[i-1][j-1] + a[i-1][j])  # Sum of the two elements above
            a.append(b)
        return a
            
