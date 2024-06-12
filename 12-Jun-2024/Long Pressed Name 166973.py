# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n = len(name)
        m = len(typed)

        l = 0  
        r = 0

        while l <= n and r < m:
            if l < n and name[l] == typed[r]:
                l += 1
                r += 1
            elif name[l-1] == typed[r] and l != 0:
                r += 1
            else:
                return False

        return l == n and r == m