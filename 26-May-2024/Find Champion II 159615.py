# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[y] = x
        

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for u, v in edges:
            uf.union(u, v)
        
        roots = set(uf.find(i) for i in range(n))
        
        if len(roots) == 1:
            root = next(iter(roots))
            return root
        else:
            return -1

