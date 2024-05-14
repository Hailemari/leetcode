# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        target = (m - 1, n - 1)
        memo = [[-1] * n for _ in range(m)]

        def inbound(x, y):
            return 0 <= x < m and 0 <= y < n

        def f(i, j):
            if (i, j) == target:
                return 1
            if not inbound(i, j):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            ans = 0
            ans += f(i + 1, j)
            ans += f(i, j + 1)

            memo[i][j] = ans
            return memo[i][j]

        return f(0, 0)