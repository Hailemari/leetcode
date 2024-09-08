# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

MAX_TEMP = 200005

n, k, q = map(int, input().split())

temp_diff = [0] * MAX_TEMP


for _ in range(n):
    l, r = map(int, input().split())
    temp_diff[l] += 1
    if r + 1 < MAX_TEMP:
        temp_diff[r + 1] -= 1

current_recommendations = 0
admissible_temps = [0] * MAX_TEMP
for i in range(MAX_TEMP):
    current_recommendations += temp_diff[i]
    admissible_temps[i] = 1 if current_recommendations >= k else 0

prefix_sum_temps = [0] * MAX_TEMP
for i in range(1, MAX_TEMP):
    prefix_sum_temps[i] = admissible_temps[i] + prefix_sum_temps[i - 1]

query_results = []
for _ in range(q):
    l, r = map(int, input().split())
    query_results.append(prefix_sum_temps[r] - (prefix_sum_temps[l - 1] if l > 1 else 0))

for res in query_results:
    print(res)
