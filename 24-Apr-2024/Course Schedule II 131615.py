# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque()
        order = []

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(order) != numCourses:
            return []
        
        return order