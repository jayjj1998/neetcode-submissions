class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        difference = 0
        R = 0

        for R in range(0, len(prices) - 1):
            for L in range(R + 1, len(prices)):
                difference = max(difference, prices[L] - prices[R])
        
        return difference