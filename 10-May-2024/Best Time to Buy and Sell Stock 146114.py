# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]

        for i in range(1, len(prices)):
            cur_profit = prices[i] - min_val
            max_profit = max(max_profit, cur_profit)
            min_val = min(min_val, prices[i])

        return max_profit