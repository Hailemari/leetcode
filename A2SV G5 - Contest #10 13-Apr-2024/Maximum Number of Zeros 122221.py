# Problem: Maximum Number of Zeros - https://codeforces.com/gym/514644/problem/D

import sys
from collections import Counter
from math import gcd
input = sys.stdin.readline
n = int(input().strip())
a =list(map(int, input().strip().split()))
b =list(map(int, input().strip().split()))
count = Counter()

ans = 0
for i in range(n):
    if a[i] == 0:
        if b[i] == 0:
            ans += 1
    else:
        x = b[i] // (gcd(abs(a[i]), abs(b[i])))
        y = a[i] // (gcd(abs(a[i]), abs(b[i])))
        if b[i] < 0:
            x *=  -1
            y *= -1
        elif b[i] == 0 and a[i] < 0:
            y *=  -1
        count[(x, y)] += 1
if len(count) == 0:
    print(ans)
else:
    print(ans + max(count.values()))
    