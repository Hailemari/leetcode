# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        
        def is_palindrome(val):
            return val == val[::-1]

        def f(i, partition):
            if i == n:
                ans.append(partition[::])
                return
     
            for j in range(i, n):
                if is_palindrome(s[i:j + 1]):
                    partition.append(s[i:j + 1])
                    f(j + 1, partition)
                    partition.pop()

        f(0, [])
        return ans
        