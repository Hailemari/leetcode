# Problem: Get Equal Substrings Within Budget - https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        max_length = 0

        l = 0
        cur_cost = 0
        for r in range(len(s)):
            cur_cost += abs(ord(s[r]) - ord(t[r]))

            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            win_size = r - l + 1
            max_length = max(max_length, win_size)


        return max_length
                
