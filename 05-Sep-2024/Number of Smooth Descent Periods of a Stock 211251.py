# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0

        l = 0
        for r in range(n):
            
            while r != 0 and prices[r] != prices[r - 1] - 1 and l < r:
                l += 1

            ans += (r - l + 1)

        return ans
            