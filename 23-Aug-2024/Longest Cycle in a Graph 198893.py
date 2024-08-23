# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        graph = defaultdict(list)
        
        for i in range(n):
            if edges[i] != -1:
                graph[i].append(edges[i])
                indegree[edges[i]] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        print(graph)
        while queue:
            cur = queue.popleft()
            for node in graph[cur]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
            del graph[cur]

        visited = set()

        ans = -1
        def dfs(node, length):
            if node in visited:
                return length
            
            visited.add(node)
            return dfs(graph[node][0], length + 1)

        for i in range(n):
            if i not in visited and i in graph:
                ans = max(ans, dfs(i, 0))

        return ans

        
        
        