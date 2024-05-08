# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefix_xor = [nums[0]] * n

        for i in range(1, n):
            prefix_xor[i] = prefix_xor[i-1] ^ nums[i]

        prefix_xor = prefix_xor[::-1]

        ans = []
        for num in prefix_xor:
            ans.append(num ^ (2 ** (maximumBit) - 1))

        return ans
                
