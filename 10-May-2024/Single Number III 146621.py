# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num

        rightmost_bit = xor & (-xor)

        x, y = 0, 0
        for num in nums:
            if num & rightmost_bit:
                x ^= num
            else:
                y ^= num

        return [x, y]