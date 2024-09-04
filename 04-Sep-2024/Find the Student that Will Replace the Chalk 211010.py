# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k = k % total

        n = len(chalk)
        for i in range(n):
            if k < chalk[i]:
                return i
            k -= chalk[i]

