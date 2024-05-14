# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        memo = {}
        def dp(i, target, memo):
            if target == 0:
                return 1
            if i == n:
                return 0

            if (i, target) in memo:
                return memo[(i, target)]

            ans = 0
            if coins[i] <= target:
                ans += dp(i, target - coins[i], memo)
            
            ans += dp(i + 1, target, memo)
            memo[(i, target)] = ans
            
            return memo[(i, target)]

        return dp(0, amount, {})