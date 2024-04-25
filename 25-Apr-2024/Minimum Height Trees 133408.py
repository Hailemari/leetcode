# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]

        def build_graph():
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
                indegree[b] += 1
                indegree[a] += 1

        build_graph()
        
        level = []

        for i in range(n):
            if indegree[i] == 1:
                level.append(i)
        
        while level:
            next_level = []

            for item in level:
                for neighbor in graph[item]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        next_level.append(neighbor)

            if not next_level:
                return level
            level = next_level
        
        return [0]
