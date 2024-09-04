# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        temp = ""
        for char in s:
            position = ord(char) - 96
            temp += str(position)
        s = temp
        
        while k:
            sum = 0
            for char in s:
                sum += int(char)
            s = str(sum)
            k -= 1

        return int(s)
            