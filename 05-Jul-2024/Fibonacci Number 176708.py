# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
            
        prev_one = 0
        prev_two = 1

        for i in range(2, n + 1):
            cur = prev_two + prev_one
            prev_one = prev_two
            prev_two = cur

        return prev_two
        