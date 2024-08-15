# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        m, n = len(targetGrid), len(targetGrid[0])
        
        color_boxes = {}
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                if color not in color_boxes:
                    color_boxes[color] = [i, j, i, j] 
                else:
                    color_boxes[color][0] = min(color_boxes[color][0], i)
                    color_boxes[color][1] = min(color_boxes[color][1], j)
                    color_boxes[color][2] = max(color_boxes[color][2], i)
                    color_boxes[color][3] = max(color_boxes[color][3], j)

        graph = defaultdict(set)
        for color, (min_row, min_col, max_row, max_col) in color_boxes.items():
            for i in range(min_row, max_row + 1):
                for j in range(min_col, max_col + 1):
                    if targetGrid[i][j] != color:
                        graph[color].add(targetGrid[i][j])

        in_degree = {color: 0 for color in color_boxes}
        for color in graph:
            for neighbor in graph[color]:
                in_degree[neighbor] += 1
        
        queue = deque([color for color in in_degree if in_degree[color] == 0])
        sorted_colors = []
        
        while queue:
            color = queue.popleft()
            sorted_colors.append(color)
            for neighbor in graph[color]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return len(sorted_colors) == len(color_boxes)