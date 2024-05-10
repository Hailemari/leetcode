# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins) - 1
        
        def f(i, target, memo):
            if target == 0:
                return 0
            if i < 0 or target < 0:
                return float('inf')

            if (i, target) in memo:
                return memo[(i, target)]

            
            take = 1 + f(i, target - coins[i], memo)
            not_take = f(i - 1, target, memo)

            memo[(i, target)] = min(take, not_take)
            return memo[(i, target)]

        answer = f(n, amount, {})
        if answer != float('inf'):
            return answer
        return -1