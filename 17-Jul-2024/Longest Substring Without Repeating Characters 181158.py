# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        l = 0
        longest = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l += 1

            longest = max(longest, r - l + 1) 

        return longest