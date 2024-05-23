# Problem: B - Grid Path - https://codeforces.com/gym/524965/problem/B

import sys
import threading


input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        
        memo = {}
        
        def f(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i == m - 1 and j == n - 1:
                return 0
            if i >= m or j >= n:
                return float('-inf')
            
           
            down = (j + 1) + f(i + 1, j)
            right = (i + 1) + f(i, j + 1)
            

            if down == k or right == k:
                result = k
            else:
                result = max(down, right)
            memo[(i, j)] = result
            return result
        
        if f(0, 0) == k:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    sys.setrecursionlimit(10000)  
    threading.stack_size(67108864) 
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()