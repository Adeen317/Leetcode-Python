class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=(int(f'{int(a)}', 2))
        y=(int(f'{int(b)}', 2))
        return str(f'{x+y:b}')
