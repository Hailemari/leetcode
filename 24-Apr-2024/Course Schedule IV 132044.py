# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        pre = defaultdict(set)

        for a, b in prerequisites:
            graph[a].append(b)
        
        def dfs(node, descendents):
            for neighbor in graph[node]:
                if neighbor not in descendents:
                    descendents.add(neighbor)
                    dfs(neighbor, descendents)

            return descendents

        for i in range(numCourses):
            descendents = set()
            pre[i] = dfs(i, descendents)


        ans = [False] * len(queries)
        for i, query  in enumerate(queries):
            a, b = query
            if b in pre[a]:
                ans[i] = True

        return ans