# Problem: A - Ascend - https://codeforces.com/gym/526229/problem/A

n = int(input())
elements = list(map(int, input().split()))

max_length = 1
sub_array = [-1]

for element in elements:
    if element > sub_array[-1]:
        sub_array.append(element)
        max_length = max(max_length, len(sub_array) - 1)
    else:
        sub_array = [-1, element]

print(max_length)
