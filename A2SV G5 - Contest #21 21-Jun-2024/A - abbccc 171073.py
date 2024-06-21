# Problem: A - abbccc - https://codeforces.com/gym/530187/problem/A

n = int(input())
t = input()

jump = 1
i = 0
res = ""

while i < n:
    res += t[i]
    i += jump
    jump += 1

print(res)