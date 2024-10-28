# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        lower_bound, upper_bound = 1, x

        while lower_bound <= upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            square = midpoint * midpoint

            if square <= x < (midpoint + 1) * (midpoint + 1):
                return midpoint
            elif square > x:
                upper_bound = midpoint - 1
            else:
                lower_bound = midpoint + 1

        return -1