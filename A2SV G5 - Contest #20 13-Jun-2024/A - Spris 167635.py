# Problem: A - Spris - https://codeforces.com/gym/528792/problem/A

a = int(input())
b = int(input())
c = int(input())

ans = 0
for i in range(a, 0, -1):
    if 2 * i <= b and 4 * i <= c:
        ans = i + 2 * i + 4 * i
        break

print(ans)