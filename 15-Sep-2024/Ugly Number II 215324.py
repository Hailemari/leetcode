# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1

        p2, p3, p5 = 0, 0, 0
        next_2, next_3, next_5 = 2, 3, 5  

        for i in range(1, n):
            next_ugly = min(next_2, next_3, next_5)
            ugly_nums[i] = next_ugly

            if next_ugly == next_2:
                p2 += 1
                next_2 = ugly_nums[p2] * 2  
            if next_ugly == next_3:
                p3 += 1
                next_3 = ugly_nums[p3] * 3 
            if next_ugly == next_5:
                p5 += 1
                next_5 = ugly_nums[p5] * 5  

        return ugly_nums[n - 1]
