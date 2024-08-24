class Solution:
    def findComplement(self, num: int) -> int:
        a=list(f'{num:b}')
        b=[]
        for i in range(len(a)):
            if a[i]=='1':
                a[i]='0'
                b.append(a[i])
            else:
                a[i]='1'
                b.append(a[i])

        x="".join(b)
        
        return int(f'{x}', 2)
        
