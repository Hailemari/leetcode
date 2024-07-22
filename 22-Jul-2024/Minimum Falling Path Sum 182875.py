# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        prev = matrix[n-1]

        for i in range(n - 2, -1, -1):
            cur = [0] * n
            for j in range(n):
                cell_num = matrix[i][j]
                down = prev[j]
                left_dig = float('inf')
                right_dig = float('inf')

                if j - 1 >= 0:
                    left_dig = prev[j - 1]

                if j + 1 < n:
                    right_dig = prev[j + 1]

                cur[j] = min(down, left_dig, right_dig) + cell_num
            prev = cur

        return min(prev)
