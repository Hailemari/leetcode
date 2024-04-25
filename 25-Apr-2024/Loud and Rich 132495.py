# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        quiet_index = {i: i for i in range(n)} 

        for a, b in richer:
            graph[b].append(a)

        def dfs(node):
            if quiet_index[node] != node:
                return quiet_index[node]
                
            for neighbor in graph[node]:
                candidate = dfs(neighbor)
                if quiet[candidate] < quiet[quiet_index[node]]:
                    quiet_index[node] = candidate
            return quiet_index[node]

        return [dfs(i) for i in range(n)]