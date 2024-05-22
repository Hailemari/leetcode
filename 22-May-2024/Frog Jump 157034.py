# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = defaultdict(set)
        dp[0].add(0)

        for i in range(len(stones)):
            for k in dp[stones[i]]:
                if k > 0:
                    dp[stones[i] + k].add(k)
                if k - 1 > 0:
                    dp[stones[i] + k - 1].add(k - 1)
                dp[stones[i] + k + 1].add(k + 1)


        return len(dp[stones[-1]]) != 0

