# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b != 0:
            sum = (a ^ b) & mask
            carry = ((a & b) << 1) & mask

            a = sum
            b = carry

        return a if a < 0x7FFFFFFF else ~(a ^ mask)