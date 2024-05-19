# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

def process_operations(n, operations):
    result = []
    heap = []

    def insert(x):
        heapq.heappush(heap, x)
        result.append(f"insert {x}")

    def remove_min():
        if not heap:
            insert(1)
        heapq.heappop(heap)
        result.append("removeMin")

    def get_min(x):
        while heap and heap[0] < x:
            remove_min()
        if not heap or heap[0] > x:
            insert(x)
        result.append(f"getMin {x}")

    for operation in operations:
        parts = operation.split()
        command = parts[0]
        
        if command == "insert":
            x = int(parts[1])
            insert(x)
        elif command == "removeMin":
            remove_min()
        elif command == "getMin":
            x = int(parts[1])
            get_min(x)
    
    return result

n = int(data[0])
operations = data[1:]
result = process_operations(n, operations)

print(len(result))
for op in result:
    print(op)
