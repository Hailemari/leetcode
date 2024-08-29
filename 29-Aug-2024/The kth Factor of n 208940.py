# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:
                    break
        
        factors.append(n)
        if len(factors) < k:
            return -1
        
        return factors[k - 1]
