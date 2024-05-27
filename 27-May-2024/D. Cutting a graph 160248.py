# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

def find_root(node):
    while node != parent[node]:
        node = parent[node]
    return node

def merge_sets(node1, node2):
    root1 = find_root(node1)
    root2 = find_root(node2)
    if root1 != root2:
        if set_size[root1] >= set_size[root2]:
            parent[root2] = root1
            set_size[root1] += set_size[root2]
        else:
            parent[root1] = root2
            set_size[root2] += set_size[root1]

vertex_count, edge_count, operation_count = map(int, input().split())
parent = {i: i for i in range(1, vertex_count + 1)}
set_size = {i: 1 for i in range(1, vertex_count + 1)}

for _ in range(edge_count):
    u, v = map(int, input().split())

operations = []
for _ in range(operation_count):
    op_type, u, v = input().split()
    operations.append([op_type, int(u), int(v)])

results = []
for i in range(operation_count - 1, -1, -1):
    op_type, u, v = operations[i]
    if op_type == "cut":
        merge_sets(u, v)
    else:
        if find_root(u) == find_root(v):
            results.append("YES")
        else:
            results.append("NO")

for result in reversed(results):
    print(result)
