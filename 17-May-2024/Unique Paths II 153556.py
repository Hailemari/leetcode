# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
    
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    left = 0
                    down = 0
                    if j + 1 < n:
                        left = dp[i][j + 1]
                    
                    if i + 1 < m:
                        down = dp[i + 1][j]

                    dp[i][j] = left + down

                if i == m - 1 and j == n - 1 and obstacleGrid[m-1][n-1] == 0:
                    dp[m-1][n-1] = 1
                    
        return dp[0][0]
                
