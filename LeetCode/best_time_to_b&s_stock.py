class Solution:
    def maxProfit(self, prices):
        buy = float('inf')
        max_profit = 0

        for price in prices:
            if price < buy:
                buy = price

            profit = price - buy

            if profit > max_profit:
                max_profit = profit

        return max_profit