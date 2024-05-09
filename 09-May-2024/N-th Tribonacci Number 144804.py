# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        prev1 = 0
        prev2 = 1
        prev3 = 1

        for i in range(3, n + 1):
            cur = prev1 + prev2 + prev3
            prev1 = prev2
            prev2 = prev3
            prev3 = cur

        if n == 0:
            return prev1
        if n == 1:
            return prev2

        return prev3