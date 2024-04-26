# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        

        def find(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def union(node_a, node_b):
            root_a = find(node_a)
            root_b = find(node_b)

            if root_a != root_b:
                if rank[root_a] < rank[root_b]:
                    root[root_a] = root_b
                elif rank[root_b] < rank[root_a]:
                    root[root_b] = root_a
                else:
                    root[root_a] = root_b
                    rank[root_b] += 1

            else:
                return [node_a, node_b]

        redundant_edge = []
        for a, b in edges:
            redundant_edge = union(a, b)
            if redundant_edge:
                return redundant_edge

        return redundant_edge
