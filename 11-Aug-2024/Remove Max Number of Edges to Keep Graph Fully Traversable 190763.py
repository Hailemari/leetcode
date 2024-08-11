# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        removable_edges = 0

        for edge_type, u, v in edges:
            if edge_type == 3:
                if not alice.union(u-1, v-1):
                    removable_edges += 1
                bob.union(u-1, v-1)

        for edge_type, u, v in edges:
            if edge_type == 1:
                if not alice.union(u-1, v-1):
                    removable_edges += 1
            elif edge_type == 2:
                if not bob.union(u-1, v-1):
                    removable_edges += 1

        if alice.components == 1 and bob.components == 1:
            return removable_edges
        return -1