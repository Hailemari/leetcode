# Problem: Interesting drink - https://codeforces.com/problemset/problem/706/B/

n = int(input())
prices = list(map(int, input().split()))
q = int(input())
prices.sort()
for _ in range(q):
    coins = int(input())
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if coins >= prices[mid]:
            low = mid + 1
        else:
            high = mid - 1


    print(low)