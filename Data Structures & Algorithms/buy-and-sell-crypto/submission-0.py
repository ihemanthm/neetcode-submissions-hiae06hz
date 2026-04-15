class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        leftMin = prices[0]
        for price in prices[1:]:
            profit = max(profit, price-leftMin)
            if price< leftMin:
                leftMin = price
        return profit