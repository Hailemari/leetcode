# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        def f(i, buy, memo):
            if i >= n:
                return 0
            if (i, buy) in memo:
                return memo[(i, buy)]

            if buy:
                profit = max(-prices[i] + f(i + 1, 0, memo), f(i + 1, 1, memo))
            else:
                profit = max(prices[i] + f(i + 2, 1, memo), f(i + 1, 0, memo))

            memo[(i, buy)] = profit
            return memo[(i, buy)]

        return f(0, 1, {})