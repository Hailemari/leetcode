# Problem: A - Distribute - https://codeforces.com/gym/524965/problem/A

import sys, threading
input = sys.stdin.readline



def main():
    n = int(input())
    arr = list(map(int, input().split()))
    sum_arr = sum(arr)
    target = sum_arr * 2 // n

    ans = set()
    visited = set()
    for i in range(n):
        for j in range(i + 1, n):
            if i in visited or j in visited:
                continue
            if arr[i] + arr[j] == target:
                visited.add(i)
                visited.add(j)
                ans.add((i, j))
                
    
    for i, j in ans:
        print(i + 1, j + 1)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


