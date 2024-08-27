# Problem: New Year Transportation - https://codeforces.com/problemset/problem/500/A

n, t = map(int, input().split())
arr = list(map(int, input().split()))

i = 1
ans = "NO"
while i <= t:
    if i == t:
        ans = "YES"
        break
    
    i += arr[i - 1]

print(ans)