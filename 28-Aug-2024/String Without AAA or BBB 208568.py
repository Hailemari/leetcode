# Problem: String Without AAA or BBB - https://leetcode.com/problems/string-without-aaa-or-bbb

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
        ans = ""
        while a > 0 and b > 0:
            if a > b:
                if a - b > 2:
                    ans += "aa"
                    a -= 2
                    ans += "b"
                    b -= 1
                else:
                    ans += "a"
                    ans += "b"
                    a -= 1
                    b -= 1

            else:
                if b - a > 2:
                    ans += "bb"
                    b -= 2                 
                    ans += "a"
                    a -= 1
                else:
                    ans += "b"
                    ans += "a"
                    b -= 1
                    a -= 1
        if a > 0:
            ans += "a" * a
        if b > 0:
            ans += "b" * b
        return ans
            