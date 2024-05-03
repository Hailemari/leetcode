# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        temp = num

        count = 0
        while temp:
            temp = temp >> 1
            count += 1
        
        return num ^ ((1 << count) - 1)