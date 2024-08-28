# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid2)
        n = len(grid2[0])

        def inbound(i, j):
            return 0 <= i < m and 0 <= j < n

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = set()
        def dfs(i, j, island):
            if not inbound(i, j):
                return
            if grid2[i][j] == 0:
                return

            visited.add((i, j))
            island.append((i, j))
            for dr, dc in directions:
                new_row = i + dr
                new_col = j + dc
                if (new_row, new_col) not in visited:
                    dfs(new_row, new_col, island)
                

            return island
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    island = dfs(i, j, [])
                    Flag = True
                    for l, r in island:
                        if grid1[l][r] != 1:
                            Flag = False
                            break

                    if Flag:
                        count += 1


        return count
