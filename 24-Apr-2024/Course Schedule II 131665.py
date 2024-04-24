# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        color = [0 for _ in range(numCourses)]
        
        for a, b in prerequisites:
            graph[b].append(a)

        stack = []
        def dfs(node):
            if color[node] == GRAY:
                return True
            
            if color[node] == BLACK:
                return False
            
            color[node] = GRAY
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True

            color[node] = BLACK
            stack.append(node)
            
            return False

        WHITE = 0
        GRAY = 1
        BLACK = 2
        for course in range(numCourses):
            if color[course] == WHITE:  
                if dfs(course):
                    return []

        return stack[::-1]