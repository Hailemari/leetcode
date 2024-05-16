# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        memo = {}
        def f(i, buy, transactions):
            if i == n:
                return 0
            if transactions == 0:
                return 0
            if (i, buy, transactions) in memo:
                return memo[(i, buy, transactions)]
            
            take = 0
            not_take = 0
            if buy:
                take = -prices[i] + f(i + 1, 0, transactions)
                not_take = f(i + 1, buy, transactions)
            else:
                take = prices[i] + f(i + 1, 1, transactions - 1)
                not_take = f(i + 1, 0, transactions)

            memo[(i, buy, transactions)] = max(take, not_take)
            return memo[(i, buy, transactions)]
        return f(0, 1, 2)