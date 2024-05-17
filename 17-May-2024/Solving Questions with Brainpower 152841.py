# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        m = len(questions)

        dp = [0] * m
        dp[-1] = questions[m - 1][0]
        for i in range(m - 2, -1, -1):
            pick = questions[i][0] 
            if i + questions[i][1] + 1 < m:
                pick += dp[i + questions[i][1] + 1]
            not_pick = dp[i + 1]

            dp[i] = max(pick, not_pick)

        return dp[0]