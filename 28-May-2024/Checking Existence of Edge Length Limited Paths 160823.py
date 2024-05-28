# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  #
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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries = sorted([(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)], key=lambda x: x[2])
        
        uf = UnionFind(n)
        edgeIndex = 0
        m = len(queries)
        result = [False] * m
        
        for p, q, limit, idx in queries:
            while edgeIndex < len(edgeList) and edgeList[edgeIndex][2] < limit:
                uf.union(edgeList[edgeIndex][0], edgeList[edgeIndex][1])
                edgeIndex += 1
            
            if uf.find(p) == uf.find(q):
                result[idx] = True
        
        return result
