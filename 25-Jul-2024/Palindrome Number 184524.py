# Problem: Palindrome Number - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        num = x
        pairs = []

        i = 0
        while num:
            rem = num % 10
            pairs.append((rem, i))
            i += 1
            num = num // 10

        temp = 0
        p1, p2 = 0, len(pairs) - 1
        while p1 <= p2:
            if p1 != p2:
                temp += (pairs[p1][0] * (10 ** pairs[p2][1]) + pairs[p2][0] * (10 ** pairs[p1][1]))
            else:
                temp += (pairs[p1][0] * (10 ** pairs[p2][1]))


            p1 += 1
            p2 -= 1

        return temp == x