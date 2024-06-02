class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        # Two variables to keep track of the previous two steps
        prev1, prev2 = 1, 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1


                
