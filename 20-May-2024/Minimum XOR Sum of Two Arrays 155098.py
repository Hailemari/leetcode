# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(i, mask):
            if i == n:
                return 0
            
            ans = float('inf')
            for j in range(n):
                if mask & (1 << j) == 0:
                    ans = min(ans, (nums1[i] ^ nums2[j]) + dp(i + 1, mask | (1 << j)))

            return ans
        n = len(nums1)
        return dp(0, 0)