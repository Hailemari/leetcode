# Problem: Find All People With Secret - https://leetcode.com/problems/find-all-people-with-secret/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[py] < self.rank[px]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
    
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x : x[2])
        
        uf = UnionFind(n)
        uf.union(0, firstPerson)

        i = 0
        while i < len(meetings):
            current_time = meetings[i][2]
            temp = []

            while i < len(meetings) and meetings[i][2] == current_time:
                x, y, _ = meetings[i]
                uf.union(x, y)
                temp.append(x)
                temp.append(y)
                i += 1

            for person in temp:
                if uf.find(person) != uf.find(0):
                    uf.parent[person] = person
                    uf.rank[person] = 0

        return [i for i in range(n) if uf.find(i) == uf.find(0)]