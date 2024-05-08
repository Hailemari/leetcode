# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

x = int(input())
 
count = 0
while x:
    count += x & 1
    x >>= 1
 
print(count)