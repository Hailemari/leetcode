# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values) - 1
        
        memo = {}
        def f(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            tot_score = float('inf')
            for k in range(i + 1, j):
                tot_score = min(tot_score, values[i] * values[j] * values[k] + f(k, j) + f(i, k))

            if tot_score == float('inf'):
                memo[(i, j)] = 0
                return memo[(i, j)]

            memo[(i, j)] = tot_score
            return memo[(i, j)]

        return f(0, n)