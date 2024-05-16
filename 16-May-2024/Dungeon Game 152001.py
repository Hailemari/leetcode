# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m - 1 and j == n - 1:
                memo[(i, j)] = max(1, 1 - dungeon[i][j])
            elif i == m - 1:
                memo[(i, j)] = max(1, dp(i, j + 1) - dungeon[i][j])
            elif j == n - 1:
                memo[(i, j)] = max(1, dp(i + 1, j) - dungeon[i][j])
            else:
                right = max(1, dp(i, j + 1) - dungeon[i][j])
                down = max(1, dp(i + 1, j) - dungeon[i][j])
                memo[(i, j)] = min(right, down)

            return memo[(i, j)]

        return dp(0, 0)