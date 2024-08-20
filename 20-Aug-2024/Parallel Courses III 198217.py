# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n)]
        in_degree = [0] * n
        
        for prev, next in relations:
            graph[prev - 1].append(next - 1)
            in_degree[next - 1] += 1
        
        dp = time[:]
        queue = deque()
        
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            
            for next_course in graph[course]:
                dp[next_course] = max(dp[next_course], dp[course] + time[next_course])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        

        return max(dp)





        