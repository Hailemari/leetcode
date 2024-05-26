# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.min = list(range(n))
        self.max = list(range(n))
        self.size = [1] * n

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
                self.size[root_u] += self.size[root_v]
                self.min[root_u] = min(self.min[root_u], self.min[root_v])
                self.max[root_u] = max(self.max[root_u], self.max[root_v])
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
                self.size[root_v] += self.size[root_u]
                self.min[root_v] = min(self.min[root_u], self.min[root_v])
                self.max[root_v] = max(self.max[root_u], self.max[root_v])
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
                self.size[root_u] += self.size[root_v]
                self.min[root_u] = min(self.min[root_u], self.min[root_v])
                self.max[root_u] = max(self.max[root_u], self.max[root_v])

    def get(self, u):
        root_u = self.find(u)
        return self.min[root_u], self.max[root_u], self.size[root_u]

import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])

uf = UnionFind(n)

output = []
index = 2
for _ in range(m):
    query = data[index]
    if query == "union":
        u = int(data[index + 1]) - 1
        v = int(data[index + 2]) - 1
        uf.union(u, v)
        index += 3
    elif query == "get":
        v = int(data[index + 1]) - 1
        result = uf.get(v)
        output.append(f"{result[0] + 1} {result[1] + 1} {result[2]}")
        index += 2

print("\n".join(output))
