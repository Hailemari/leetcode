# Problem: Minimum Difference Between Largest and Smallest Value in 3 Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        n = len(nums)

        diff1 = nums[n-1] - nums[3]
        diff2 = nums[n-2] - nums[2]
        diff3 = nums[n-3] - nums[1]
        diff4 = nums[n-4] - nums[0]

        return min(diff1, diff2, diff3, diff4)