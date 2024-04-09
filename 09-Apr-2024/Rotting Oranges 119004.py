# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols

        initial_rottens = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    initial_rottens.append((i, j))
        
        # if not initial_rottens:
        #     return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = deque()
        for rotten in initial_rottens:
            queue.append(rotten)
        
        ans = -1
        while queue:
            n = len(queue)
            for _ in range(n):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        queue.append((new_row, new_col))
                        grid[new_row][new_col] = 2
            
            ans += 1

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        return ans if ans != -1 else 0

    