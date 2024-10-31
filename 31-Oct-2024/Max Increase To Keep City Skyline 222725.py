# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_increase = 0

        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        for i in range(n):
            for j in range(n):
                max_increase += min(row_max[i], col_max[j]) - grid[i][j]
                
        return max_increase
