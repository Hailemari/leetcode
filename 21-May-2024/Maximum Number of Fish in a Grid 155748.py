# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n
        
        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            res = grid[r][c] + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r - 1, c) + dfs(r + 1, c)

            return res


        visited = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))



        return ans