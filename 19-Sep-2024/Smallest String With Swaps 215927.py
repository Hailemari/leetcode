# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        
        for index1, index2 in pairs:
            graph[index1].append(index2)
            graph[index2].append(index1)

        def find_component(start, visited):
            queue = deque([start])
            component = []
            visited[start] = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return component

        visited = [False] * len(s)
        connected_components = []
        
        for i in range(len(s)):
            if not visited[i]:
                component = find_component(i, visited)
                connected_components.append(component)

        s = list(s)
        
        for component in connected_components:
            sorted_indices = sorted(component)
            sorted_chars = sorted(s[index] for index in sorted_indices)
            
            for index, char in zip(sorted_indices, sorted_chars):
                s[index] = char

        return ''.join(s)