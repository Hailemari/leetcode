# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        for a, b in pairs:
            graph[a].append(b)
            graph[b].append(a)

        def bfs(node, visited, graph):
            queue = deque([node])
            component = []
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

                component.append(current)

            return component

        visited = [False] * len(s)
        components = []
        for i in range(len(s)):
            if not visited[i]:
                visited[i] = True
                component = bfs(i, visited, graph)
                components.append(component)
            
        s = list(s)
        for component in components:
            indices = sorted(component)
            chars = sorted(s[i] for i in indices)
            for i, char in zip(indices, chars):
                s[i] = char

        return ''.join(s)