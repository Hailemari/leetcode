# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        

        new_array = [0] * n
        j = 0
        for i in range(n):
            if nums[i] != 0:
                new_array[j] = nums[i]
                j += 1

        return new_array
