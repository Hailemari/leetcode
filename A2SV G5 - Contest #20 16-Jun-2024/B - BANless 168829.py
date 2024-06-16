# Problem: B - BANless - https://codeforces.com/gym/528792/problem/B

for _ in range(int(input())):
        n = int(input())
        pairs = []
        
        start, end = 1, 3 * n 
        while start < end:
            pairs.append([start, end])
            start += 3
            end -= 3    

        print(len(pairs))
        for pair in pairs:
            print(*pair) 