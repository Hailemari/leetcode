# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bucket_1, bucket_2 = 0, 0

        for i in range(len(nums)):
            bucket_1 = (bucket_1 ^ nums[i]) & ~bucket_2
            bucket_2 = (bucket_2 ^ nums[i]) & ~bucket_1

        return bucket_1
