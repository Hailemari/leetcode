# Problem: Alien Dictionary ( GeeksforGeeks ) - https://www.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque

class Solution:
    def findOrder(self, alien_dict, N, K):
        graph = defaultdict(set)
        indegree = {chr(i + ord('a')): 0 for i in range(K)}
     
        for i in range(N - 1):
            first, second = alien_dict[i], alien_dict[i + 1]
            min_len = min(len(first), len(second))
            for j in range(min_len):
                if first[j] != second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break

 
        queue = deque([char for char in indegree if indegree[char] == 0])
        order = []

        while queue:
            cur = queue.popleft()
            order.append(cur)
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == K:
            return ''.join(order)
        else:
            return ""