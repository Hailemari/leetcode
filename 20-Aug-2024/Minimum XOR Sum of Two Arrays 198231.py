# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        @lru_cache(None)
        def dp(i, mask):
            if i == n:
                return 0
            
            ans = float('inf')
            
            for j in range(n):
                if not (mask & (1 << j)):
                    res = nums1[i] ^ nums2[j]
                    ans = min(ans, res + dp(i + 1, mask | (1 << j)))

            return ans

        return dp(0, 0)