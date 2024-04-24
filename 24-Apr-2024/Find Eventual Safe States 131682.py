# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                safe_nodes.add(i)

        WHITE = 0
        GRAY = 1
        BLACK = 2
        color = [WHITE for _ in range(len(graph))]
        def dfs(node):
            if color[node] == GRAY:
                return False
            if color[node] == BLACK:
                return True

            color[node] = GRAY
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            color[node] = BLACK
            return True
            
        ans = []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        


        ans.sort()
        return ans