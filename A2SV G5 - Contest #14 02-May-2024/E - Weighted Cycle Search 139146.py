# Problem: E - Weighted Cycle Search - https://codeforces.com/gym/520688/problem/E

from collections import defaultdict
from sys import stdin


def input(): 
    return stdin.readline().strip()


class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, v):
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v
    
    def merge(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    adjacency = defaultdict(list)
    for __ in range(M):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        edges.append((w, u, v))
        adjacency[u].append(v)
        adjacency[v].append(u)

    edges.sort(key=lambda edge: edge[0], reverse=True)
    dsu = DisjointSetUnion(N)
    for w, u, v in edges:
        if not dsu.merge(u, v):
            ans = (w, u, v)

    min_weight, start, end = ans
    stack = [start]

    # DFS to get the cycle
    parent = [-1] * N
    parent[start] = start
    while stack:
        vertex = stack.pop()
        for child in adjacency[vertex]:
            if vertex == start and child == end: 
                continue
            if child == end:
                parent[child] = vertex
                stack = []
                break
            if parent[child] == -1:
                parent[child] = vertex
                stack.append(child)
    vertex = end
    path = []
    while parent[vertex] != vertex:
        path.append(vertex)
        vertex = parent[vertex]
    path.append(start)

    print(min_weight, len(path))
    for i in range(len(path)):
        path[i] += 1
    print(*path)
