# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def fractionAddition(self, expression: str) -> str:
        i = 0
        num = 0
        denom = 1
        
        while i < len(expression):
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1

            numerator = 0
            while i < len(expression) and expression[i].isdigit():
                numerator = numerator * 10 + int(expression[i])
                i += 1
            numerator *= sign
            
            i += 1
  
            denominator = 0
            while i < len(expression) and expression[i].isdigit():
                denominator = denominator * 10 + int(expression[i])
                i += 1

            num = num * denominator + numerator * denom
            denom *= denominator
            
            common_divisor = gcd(abs(num), denom)
            num //= common_divisor
            denom //= common_divisor
 
        if denom < 0:
            num = -num
            denom = -denom
        
        return f"{num}/{denom}"