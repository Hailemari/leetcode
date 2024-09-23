# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [[0] * 2 for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            dp[i][0] = max(-prices[i] + dp[i + 1][1], dp[i + 1][0])
            dp[i][1] = max(prices[i] + (dp[i + 2][0] if i + 2 <= n else 0), dp[i + 1][1])

        return dp[0][0]
