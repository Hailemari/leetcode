# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

import math

def preprocess(max_value):
    divisors = {}
    for x in range(2, max_value.bit_length() + 1):
        value = (1 << x) - 1
        if value <= max_value:
            largest_divisor = 1
            for d in range(2, int(math.sqrt(value)) + 1):
                if value % d == 0:
                    largest_divisor = max(largest_divisor, value // d)
            divisors[value] = largest_divisor
    return divisors

def solve_queries(queries, divisors):
    results = []
    for a in queries:
        if a in divisors:
            results.append(divisors[a])
        else:
            x = a.bit_length()
            results.append((1 << x) - 1)
    return results


q = int(input()) 
queries = [int(input()) for _ in range(q)]

max_value = max(queries)
divisors = preprocess(max_value)

results = solve_queries(queries, divisors)

for result in results:
    print(result)
