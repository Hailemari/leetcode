# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        def bfs(row, col):
            queue = deque([(row, col)])
            board[row][col] = 'S' 

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if inbound(new_row, new_col) and board[new_row][new_col] == 'O':
                        board[new_row][new_col] = 'S'
                        queue.append((new_row, new_col))

        for i in range(m):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][n-1] == 'O':
                bfs(i, n-1)

        for j in range(n):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[m-1][j] == 'O':
                bfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'