# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = nums[0]

        for i in range(1, len(nums)):
            xor = xor ^ nums[i]

        count = 0
        ans = xor ^ k
        while ans:
            if ans | 1 == ans:
                count += 1
            ans = ans >> 1

        return count


        