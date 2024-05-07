# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

t = int(input())

for _ in range(t):
    x = int(input())
    
    y = x & -x
    if y ^ x:
        print(y)
    else:
        x = ~x
        z = x & -x
        print(y + z)