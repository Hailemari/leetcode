# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, prev = float('inf'), memo={}):
            if (i, j, prev) in memo:
                return memo[(i, j, prev)]
            if not inbound(i, j):
                return 0
            if matrix[i][j] >= prev:
                return 0
            
            longest_path = 0
            for dr, dc in directions:
                cur_path = 1 + dfs(dr + i, dc + j, matrix[i][j], memo)
                longest_path = max(longest_path, cur_path)


            memo[(i, j, prev)] = longest_path
            return longest_path

        longest_path = float('-inf')
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))

        if n == 1 and m == 1:
            return 1
        return longest_path 
