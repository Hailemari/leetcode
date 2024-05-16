# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles) - 1
        total = sum(piles)
        
        memo = {}
        def f(i, j, turn):
            if i > j:
                return 0

            if (i, j, turn) in memo:
                return memo[(i, j, turn)]

            if turn:
                first = piles[i] + f(i + 1, j, 0)
                last = piles[j] + f(i, j - 1, 0)
            else:
                first = -piles[i] + f(i + 1, j, 1)
                last = -piles[j] + f(i, j - 1, 1)

            memo[(i, j, turn)] = max(first, last)
            return memo[(i, j, turn)]

        return f(0, n, 1)