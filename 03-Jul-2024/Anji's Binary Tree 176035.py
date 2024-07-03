# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C

def read_test_case():
    n = int(input())
    s = input()
    tree = [list(map(int, input().split())) for _ in range(n)]
    return n, s, tree

def process_tree(n, s, tree):
    result = n
    stack = [(0, 0)]

    while stack:
        node, count = stack.pop()
        left, right = tree[node]

        if left == 0 and right == 0:
            result = min(result, count)
            continue

        if left:
            stack.append((left - 1, count + (s[node] != "L")))
        if right:
            stack.append((right - 1, count + (s[node] != "R")))

    return result

def main():
    results = []
    test_cases = int(input())
    
    for _ in range(test_cases):
        n, s, tree = read_test_case()
        result = process_tree(n, s, tree)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
