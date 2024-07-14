# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        flat_board = [0]
        for i in range(n - 1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                flat_board.extend(board[i])
            else:
                flat_board.extend(reversed(board[i]))
        
        
        queue = deque([(1, 0)]) # (current square, number of moves)
        visited = set()
        visited.add(1)

        while queue:
            curr_square, moves = queue.popleft()

            if curr_square == target:
                return moves
            
            for i in range(1, 7):
                next_square = curr_square + i
                if next_square <= target:
                    next_square = flat_board[next_square] if flat_board[next_square] != -1 else next_square
                    if next_square not in visited:
                        visited.add(next_square)
                        queue.append((next_square, moves + 1))

        return -1 