# Problem: C - Balanced Parentheses Clusters - https://codeforces.com/gym/520688/problem/C

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, 2 * n):
        if s[i] == "(" and s[i - 1] == "(":
            ans += 1

    print(ans)