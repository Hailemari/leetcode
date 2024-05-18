# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}

        max_len = 1
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            if dp[num] > max_len:
                max_len = dp[num]

        return max_len
        