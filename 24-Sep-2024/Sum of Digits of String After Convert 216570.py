# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = ''.join(str(ord(char) - ord('a') + 1) for char in s)
        
        for _ in range(k):
            s = str(sum(int(char) for char in s))

        return int(s)
