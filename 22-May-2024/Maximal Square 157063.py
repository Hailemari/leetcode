# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        

        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][n-1] = int(matrix[i][n-1])
        for j in range(n):
            dp[m-1][j] = int(matrix[m-1][j])


        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                down = dp[i + 1][j]
                right = dp[i][j + 1]
                diagonal = dp[i + 1][j + 1]

                dp[i][j] = 0
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(down, right, diagonal)
        
        max_val = 0
        for i in range(m):
            for j in range(n):
                max_val = max(max_val, dp[i][j])


        return max_val ** 2

