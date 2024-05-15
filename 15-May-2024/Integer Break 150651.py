# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        
        def dp(n, memo):
            if n == 1:
                return 1

            if n in memo:
                return memo[n]

            max_product = 0
            for i in range(1, n):
                max_product = max(max_product, i * (n - i), i * dp(n - i, memo))

            memo[n] = max_product
            return memo[n]

        
        memo = {}
        return dp(n, memo)


