# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:        
        m, n = len(mat), len(mat[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                else:
                    mat[i][j] = -1 

        while queue:
            row, col, distance = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if inbound(new_row, new_col) and mat[new_row][new_col] == -1:
                    mat[new_row][new_col] = distance + 1
                    queue.append((new_row, new_col, distance + 1))
        
        return mat
