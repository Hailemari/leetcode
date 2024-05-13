# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n

        def dp(i):
            if i >= n:
                return 0

            if memo[i] == 0:
                memo[i] = 1
                for j in range(i + 1, n):
                    if nums[j] > nums[i]:
                        memo[i] = max(1 + dp(j), memo[i])
                        
            return memo[i]

        max_len = 0
        for i in range(n):
            max_len = max(dp(i), max_len)

        return max_len