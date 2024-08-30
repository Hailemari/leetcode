# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        index = -1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                index = mid
                break

        if index == -1:
            return [-1, -1]
        
        print(index)
        start = index
        for i in range(index, 0, -1):
            if nums[i] == nums[i - 1]:
                start -= 1
            else:
                break
            
        end = index
        for i in range(index, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                end += 1
            else:
                break


        return [start, end]


        