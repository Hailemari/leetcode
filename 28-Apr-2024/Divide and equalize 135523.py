# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict

def add_divs(x, divs):
    i = 2
    while i * i <= x:
        while x % i == 0:
            divs[i] += 1
            x //= i
        i += 1
    if x > 1:
        divs[x] += 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    divs = defaultdict(int)
    for x in a:
        add_divs(x, divs)
    for count in divs.values():
        if count % n != 0:
            return False
    return True

t = int(input())
for _ in range(t):
    print("YES" if solve() else "NO")