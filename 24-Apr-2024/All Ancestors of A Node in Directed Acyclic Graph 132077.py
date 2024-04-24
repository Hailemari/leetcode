# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ancenstors = defaultdict(set)

        for a, b in edges:
            graph[b].append(a)
        
        def dfs(node, ancestor):
            for neighbor in graph[node]:
                if neighbor not in ancestor:
                    ancestor.add(neighbor)
                    dfs(neighbor, ancestor)

            return ancestor

        ans = []
        for i in range(n):
            ancestor = dfs(i, set())
            ancestor = list(ancestor)
            ancestor.sort()
            ans.append(ancestor)

        return ans