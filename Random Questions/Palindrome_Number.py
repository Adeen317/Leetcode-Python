class Solution:
    def isPalindrome(self, x: int) -> bool:
        x1=str(x)
        return x1==x1[::-1]
        
