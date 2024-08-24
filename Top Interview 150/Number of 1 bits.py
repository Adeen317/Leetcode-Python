class Solution:
    def hammingWeight(self, n: int) -> int:
        a=(list(f'{n:032b}'))
        b=[]
        for i in range(len(a)):
            if a[i]=='1':
                b.append(a[i])
        return len(b)
        
