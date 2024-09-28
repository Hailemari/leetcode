# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        edges = [(manhattan_distance(points[i], points[j]), i, j) for i in range(n) for j in range(i + 1, n)]
        edges.sort()

        parent = list(range(n))
        rank = [0] * n
        mst_cost, count = 0, 0

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                return True
            return False

        for cost, u, v in edges:
            if union(u, v):
                mst_cost += cost
                count += 1
                if count == n - 1:
                    break

        return mst_cost
