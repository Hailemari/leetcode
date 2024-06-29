# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])  
            return parent[node]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                if rank[root_a] > rank[root_b]:
                    parent[root_b] = root_a
                elif rank[root_a] < rank[root_b]:
                    parent[root_a] = root_b
                else:
                    parent[root_b] = root_a
                    rank[root_a] += 1

        
        for a, b in edges:
            union(a, b)

        par = [[] for _ in range(n)]
        for i in range(n):
            par[find(i)].append(i)

        ans = 0
        total = n
        for ls in par:
            length = len(ls)
            if length > 0:
                ans += (total - length ) * length
                total -= length

        return ans