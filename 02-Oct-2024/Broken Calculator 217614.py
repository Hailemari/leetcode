# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target > startValue:
            count += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

        operations = count + startValue - target
        return operations







