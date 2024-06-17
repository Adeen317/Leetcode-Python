class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a=int(dividend/divisor)
        if dividend < -2**31 and divisor==-1:
            return 2**31-1

        if a < -2**31:
            return -2**31
        elif a > ((2**31)-1):
            return ((2**31)-1)
        else:
            return a
