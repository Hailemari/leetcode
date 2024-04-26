# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(node):
            if node != root[node]:
                root[node] = find(root[node]) 
            return root[node]

        def union(node_a, node_b):
            root_a = find(node_a)
            root_b = find(node_b)

            if root_a != root_b:
                if rank[root_a] < rank[root_b]:
                    root[root_a] = root_b
                elif rank[root_b] < rank[root_a]:
                    root[root_b] =  root_a
                else:
                    root[root_a] = root_b
                    rank[root_b] += 1

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union(i, j)

        
        res = set()
        for i in range(n):
            res.add(find(i))

        return len(res)