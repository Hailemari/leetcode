# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [0]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            cur = triangle[i]
            for j in range(len(triangle[i])):
                top = float('inf')
                if j < len(triangle[i - 1]):
                    top = dp[j]
                top_left = float('inf')
                if j - 1 >= 0:
                    top_left = dp[j - 1]
                cur[j] = triangle[i][j] + min(top, top_left)

            dp = cur

        return min(dp)