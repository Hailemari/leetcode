# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        positive_diagonal = set()
        negative_diagonal = set()
        
        def canPlace(r, c):
            if c in col or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                return False
            return True
            
        solutions = 0
        def backtrack(r):
            nonlocal solutions

            if r == n:
                solutions += 1
                return

            for c in range(n):
                if not canPlace(r, c):
                    continue
                    
                col.add(c)
                positive_diagonal.add(r + c)
                negative_diagonal.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                positive_diagonal.remove(r + c)
                negative_diagonal.remove(r - c)

        backtrack(0)

        return solutions