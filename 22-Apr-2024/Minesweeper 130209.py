# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        rows = len(board)
        cols = len(board[0])
        
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        def dfs(r, c):
            if board[r][c] == 'M':
                board[r][c] = 'X'
                return 
            if board[r][c] == 'E':
                mines = 0
                for dr, dc in directions:
                    new_row, new_col = dr + r, dc + c
                    if inbound(new_row, new_col) and board[new_row][new_col] == 'M':
                        mines += 1

                if mines == 0:
                    board[r][c] = 'B'
                    for dr, dc in directions:
                        new_row, new_col = dr + r, dc + c
                        if inbound(new_row, new_col) and board[new_row][new_col] == 'E':
                            dfs(new_row, new_col)

                else:
                    board[r][c] = str(mines)
            

        row, col = click
        if board[row][col] == 'M':
            board[row][col] = 'X'
        else:
            dfs(row, col)

        return board