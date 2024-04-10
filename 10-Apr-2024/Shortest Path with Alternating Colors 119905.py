# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in redEdges:
            graph[u].append((v, 'red'))
        for u, v in blueEdges:
            graph[u].append((v, 'blue'))

        queue = deque([(0, 'red'), (0, 'blue')])
        visited = set(queue)

        shortest_paths = [-1] * n
        distance = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node, color = queue.popleft()

                if shortest_paths[node] == -1:
                    shortest_paths[node] = distance

                opposite_color = 'red' if color == 'blue' else 'blue'
                for neighbor, edge_color in graph[node]:
                    if edge_color == opposite_color and (neighbor, opposite_color) not in visited:
                        visited.add((neighbor, opposite_color))
                        queue.append((neighbor, opposite_color))

            distance += 1

        return shortest_paths