# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        unique = set([nums[0]])

        moves = 0
        prev = nums[0]
        for i in range(1, n):
            if nums[i] in unique:
                moves += (prev + 1 - nums[i])
                unique.add(prev + 1)
                prev += 1
            else:
                prev = nums[i]
                unique.add(nums[i])
        
        return moves