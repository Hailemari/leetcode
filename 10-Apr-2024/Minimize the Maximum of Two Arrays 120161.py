# Problem: Minimize the Maximum of Two Arrays - https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

import math

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int: 
        d1 = divisor1
        d2 = divisor2
        u1 = uniqueCnt1
        u2 = uniqueCnt2

        left = 1
        right = 10**10
        result = float('inf')

       
        while left <= right:
            mid = (left + right) // 2
            count1 = mid - mid // d1
            count2 = mid - mid // d2
            count_common = mid - mid // math.lcm(d1, d2)

            if count1 < u1 or count2 < u2 or count_common < u1 + u2:
                left = mid + 1
            else:
                result = min(result, mid)
                right = mid - 1

        return result