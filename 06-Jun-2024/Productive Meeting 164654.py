# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

from heapq import heapify, heappop, heappush

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    max_heap = []
    for i in range(n):
        if arr[i] > 0:
            max_heap.append((-1 * arr[i], i + 1))

    heapify(max_heap)
    results = []
    while len(max_heap) > 1:
        power1, idx1 = heappop(max_heap)
        power2, idx2 = heappop(max_heap)
        power1, power2 = power1 * -1, power2 * -1

        results.append((idx2, idx1))
        power1 -= 1
        power2 -= 1
        if power1 > 0:
            heappush(max_heap, (power1 * -1, idx1))

        if power2 > 0:
            heappush(max_heap, (power2 * -1, idx2))

    print(len(results))
    for idx1, idx2 in results:
        print(idx1, idx2)
