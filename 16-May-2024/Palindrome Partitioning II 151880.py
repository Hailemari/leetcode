# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        def is_palindrome(i, j):
            val = s[i:j + 1]
            return val == val[::-1]

        dp = [-1] * n
        def f(i):
            if i == n:
                return 0
            
            if dp[i] != -1:
                return dp[i]

            min_cut = float('inf')
            for j in range(i, n):
                if is_palindrome(i, j):
                   min_cut = min(min_cut, 1 + f(j + 1))

            dp[i] = min_cut
            return dp[i]

        return f(0) - 1
        