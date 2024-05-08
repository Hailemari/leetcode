# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n, m, k = map(int, input().split())

armies = []
for _ in range(m + 1):
    army = int(input())
    armies.append(army)

count = 0
for i in range(m):
    xor = armies[m] ^ armies[i]
    
    set_bits = 0
    while xor:
        set_bits += xor & 1
        xor >>= 1
    if set_bits <= k:
        count += 1

print(count)
