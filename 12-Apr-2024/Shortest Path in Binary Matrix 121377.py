# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)
        target = (n - 1, n - 1)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n

        
        def bfs(row, col, clear_path):
            queue = deque([(row, col, 1)])
            visited = {(0, 0)}
            
            while queue:
                r, c, dis = queue.popleft()
                
                if (r, c) == target:
                    return dis

                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col, dis + 1))
                        visited.add((new_row, new_col))

        

            return -1

        return bfs(0, 0, 0)

        