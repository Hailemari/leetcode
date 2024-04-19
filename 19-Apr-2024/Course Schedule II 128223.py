# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        order = []

        for course, pre_requisite in prerequisites:
            graph[pre_requisite].append(course)

        WHITE = 0
        GRAY = 1
        BLACK = 2
        colors = [WHITE for _ in range(numCourses)]

        def dfs(node):
            if colors[node] == GRAY:
                return False
           
            if colors[node] == BLACK:
                return True
            
            colors[node] = GRAY
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            colors[node] = BLACK
            order.append(node)

            return True

        for i in range(numCourses):
            if colors[i] == WHITE:
                if not dfs(i):
                    return []

        return order[::-1]


