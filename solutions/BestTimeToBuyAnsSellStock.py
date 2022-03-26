class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit  = 0
        minPrice = 10000
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price-minPrice)
        return maxProfit
        
