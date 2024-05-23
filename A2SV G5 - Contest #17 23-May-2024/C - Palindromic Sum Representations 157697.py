# Problem: C - Palindromic Sum Representations - https://codeforces.com/gym/524965/problem/C

def generate_palindromes(limit):
    palindromes = set()
    for i in range(1, 10):
        palindromes.add(i)

    for length in range(2, 6):  
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        for half in range(start, end):
            half_str = str(half)
            if length % 2 == 0:
                full_str = half_str + half_str[::-1]
            else:
                full_str = half_str + half_str[-2::-1]
            pal_num = int(full_str)
            if pal_num <= limit:
                palindromes.add(pal_num)
    return sorted(palindromes)


def main():
    import sys, threading
    input = sys.stdin.readline  
    t = int(input())
    
    max_num = 0
    queries = []
    for _ in range(t):
        n = int(input())
        max_num = max(max_num, n)
        queries.append(n)
    
    MOD = 10**9 + 7
    palindromes = generate_palindromes(max_num)
   
    answers = [0] * (max_num + 1)
    answers[0] = 1
    for pal in palindromes:
        for j in range(pal, max_num + 1):
            answers[j] = (answers[j] + answers[j - pal]) % MOD
    
    result = []
    for n in queries:
        result.append(str(answers[n]))
    print("\n".join(result))

if __name__ == "__main__":
    main()