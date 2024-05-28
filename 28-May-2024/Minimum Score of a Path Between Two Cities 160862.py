# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n + 1)

        
        min_score = float('inf')
        for a, b, d in roads:
            uf.union(a, b)

        for a, b, d in roads:
            if uf.find(a) == uf.find(b) == uf.find(1):
                min_score = min(min_score, d)
                
        
        return min_score


            