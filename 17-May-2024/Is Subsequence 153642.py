# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        @cache
        def f(i, j):
            if i == len(s):
                return True
            if j == len(t):
                return False

            if s[i] == t[j]:
                return f(i + 1, j + 1)
            else:
                return f(i, j + 1)
    
            
        return f(0, 0)
        