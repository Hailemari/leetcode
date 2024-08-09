# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.sum = [0] * n

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
            self.sum[py] += self.sum[px]
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.sum[px] += self.sum[py]
        else:
            self.parent[py] = px
            self.sum[px] += self.sum[py]
            self.rank[px] += 1

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        answer = [0] * n
        max_sum = 0
        
        for i in range(n - 1, 0, -1):
            idx = removeQueries[i]
            uf.sum[idx] = nums[idx]
            
            if idx > 0 and uf.sum[uf.find(idx - 1)] > 0:
                uf.union(idx, idx - 1)
            if idx < n - 1 and uf.sum[uf.find(idx + 1)] > 0:
                uf.union(idx, idx + 1)
            
            max_sum = max(max_sum, uf.sum[uf.find(idx)])
            answer[i - 1] = max_sum
        
        return answer