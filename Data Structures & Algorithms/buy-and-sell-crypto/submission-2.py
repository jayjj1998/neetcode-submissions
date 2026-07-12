class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        lowest = prices[0]

        for price in prices:
            if price < lowest:
                lowest = price
            else:
                max_diff = max(price - lowest, max_diff)
        
        return max_diff