# Problem: Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(i, j, num):
            for k in range(9):
                if board[k][j] == num or board[i][k] == num or board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] == num:
                    return False
            return True    

        def solve(i, j):
            if i == 9:
                return True
            if j == 9:
                return solve(i + 1, 0)

            if board[i][j] == '.':
                for k in range(1, 10):
                    if is_valid(i, j, str(k)):
                        board[i][j] = str(k)
                        if solve(i, j + 1):
                            return True
                        board[i][j] = '.'
                return False
                
            return solve(i, j + 1)        

        solve(0, 0)