class Solution:
    def maxProfit(self, prices):
        buy = float('inf')
        sell = 0

        for price in prices:
            if price < buy:
                buy = price

            profit = price - buy

            if profit > sell:
                sell = profit

        return sell