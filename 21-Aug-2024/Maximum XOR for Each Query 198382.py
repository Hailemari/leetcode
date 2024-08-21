# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        total_xor = 0
        max_k_val = (1 << maximumBit) - 1

        for num in nums:
            total_xor ^= num

        res = []
        for i in range(n):
            actual_k_val = total_xor ^ max_k_val
            total_xor ^= nums[n - i - 1]
            res.append(actual_k_val)
        
        return res
