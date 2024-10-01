# Problem: Valid Triangle Number - https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        num_triplets = 0

        for j in range(n - 1, 1, -1):
            l = 0
            r = j - 1

            while l < r:
                if nums[l] + nums[r] > nums[j]:
                    num_triplets += r - l
                    r -= 1
                else:
                    l += 1

        return num_triplets
