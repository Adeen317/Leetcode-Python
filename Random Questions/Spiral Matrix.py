class Solution:
    def spiral(self,matrix, m, n, result, r, c, dr, dc):
        if m==0 or n ==0:
            return 
        for i in range(n):
            r+=dr
            c+=dc
            result.append(matrix[r][c])
        self.spiral(matrix,n, m-1, result, r, c, dc, -dr)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r=0
        c=0
        result=[]
        self.spiral(matrix, len(matrix), len(matrix[0]), result, 0, -1, 0, 1)
        return result
