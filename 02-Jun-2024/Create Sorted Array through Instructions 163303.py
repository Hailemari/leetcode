# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, nums: List[int]) -> int:
        cost = {i: [0, 0] for i in range(len(nums))}

        def merge_and_count(left, right):
            left_index = len(left) - 1
            right_index = len(right) - 1
            while left_index > -1 and right_index > -1:
                if nums[left[left_index]] <= nums[right[right_index]]:
                    cost[right[right_index]][1] += (len(left) - 1) - left_index
                    right_index -= 1
                else:
                    left_index -= 1

            while right_index > -1:
                cost[right[right_index]][1] += len(left)
                right_index -= 1  

            left_index = 0
            right_index = 0
            merged = []
            while left_index < len(left) and right_index < len(right):
                if nums[left[left_index]] < nums[right[right_index]]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    cost[right[right_index]][0] += left_index
                    merged.append(right[right_index])
                    right_index += 1

            while right_index < len(right):
                cost[right[right_index]][0] += left_index
                merged.append(right[right_index])
                right_index += 1

            merged.extend(left[left_index:])
            return merged
            
        def divide_and_merge(start, end, indices):
            if start == end:
                return [indices[end]]
            
            mid = (start + end) // 2
            left_part = divide_and_merge(start, mid, indices)
            right_part = divide_and_merge(mid + 1, end, indices)
            return merge_and_count(left_part, right_part)
        
        divide_and_merge(0, len(nums) - 1, [i for i in range(len(nums))])

        total_cost = 0
        for i in cost.keys():
            total_cost += min(cost[i])

        return total_cost % ((10**9) + 7)
