# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = matrix[m-1]

        for i in range(m - 2, -1, -1):
            cur = [0] * n
            for j in range(n - 1, -1, -1):
                left_dg = float('inf')
                right_dg = float('inf')
                if j + 1 < n:
                    right_dg = dp[j + 1]
                if j - 1 >= 0:
                    left_dg = dp[j - 1]

                down = dp[j]

                cur[j] = matrix[i][j] + min(right_dg, left_dg, down)
            dp = cur

        return min(dp)

                