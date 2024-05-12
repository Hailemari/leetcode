# Problem: C. Given Length and Sum of Digits... - https://codeforces.com/contest/489/problem/C

m, s = map(int, input().split())

if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
else:
    b = ''
    for i in range(m):
        t = min(s, 9)
        b += str(t)
        s -= t

    if s > 0:
        print("-1 -1")
    else:
        a = b[::-1]
        i = 0
        while a[i] == '0':
            i += 1
        a = list(a)
        a[i] = str(int(a[i]) - 1)
        a[0] = str(int(a[0]) + 1)
        a = ''.join(a)
        print(a, b)
