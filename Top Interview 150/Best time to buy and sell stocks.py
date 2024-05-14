class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minimum = prices[0]
        maximum = 0

        for price in prices:
            minimum = min(minimum, price)
            maximum = max(maximum, price - minimum)
        return maximum
            
