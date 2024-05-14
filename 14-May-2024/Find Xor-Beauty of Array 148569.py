# Problem: Find Xor-Beauty of Array - https://leetcode.com/problems/find-xor-beauty-of-array/

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        xor = nums[0]

        for i in range(1, len(nums)):
            xor ^= nums[i]

        return xor