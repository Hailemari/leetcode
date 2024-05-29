# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if a == b:
                ans[i] = a
            elif heights[max(a, b)] > heights[min(a, b)]:
                ans[i] = max(a, b)

                
        queries = sorted([(max(a, b), max(heights[a], heights[b]), i) for i, (a, b) in enumerate(queries) if ans[i] == -1], key=lambda x: -x[0])
        s = []
        for i, h, idx in queries:
            while i + 1 < len(heights):
                g = heights.pop()
                while s and -s[-1][0] <= g:
                    s.pop()
                s.append((-g, len(heights)))
            p = bisect_left(s, (-h, -1)) - 1
            if p >= 0:
                ans[idx] = s[p][1]
        return ans        