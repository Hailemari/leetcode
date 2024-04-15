# Problem: E - Chasing Parity - https://codeforces.com/gym/517685/problem/E

import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))

graph = defaultdict(list)

for i in range(n):
    left_bound, right_bound = i - arr[i], i + arr[i]
    if left_bound > -1:
        graph[left_bound].append(i)
    if right_bound < n:
        graph[right_bound].append(i)
    
def bfs(start_nodes, end_nodes):
    distances = [-1] * n
    queue = deque()
    for node in start_nodes:
        queue.append(node)
        distances[node] = 0
    while queue:
        current_node = queue.popleft()
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_node] + 1
                queue.append(neighbor)
    for node in end_nodes:
        ans[node] = distances[node]

odd_indices = []
even_indices = []

for i, element in enumerate(arr):
    if element % 2:
        odd_indices.append(i)
    else:
        even_indices.append(i)


ans = [-1] * n

bfs(odd_indices, even_indices)
bfs(even_indices, odd_indices)
t
print(*ans)
