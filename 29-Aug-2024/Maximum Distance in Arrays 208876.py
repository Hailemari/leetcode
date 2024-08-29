# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        min_val = (float('inf'), -1)
        max_val = (float('-inf'), -1)
        for i in range(m):
            if arrays[i][0] < min_val[0]:
                min_val = (arrays[i][0], i)
            if arrays[i][-1] > max_val[0]:
                max_val = (arrays[i][-1], i)

        if min_val[1] != max_val[1]:
            return abs(max_val[0] - min_val[0])
                
        arrays.pop(min_val[1])
        
        second_min_val = float('inf')
        second_max_val = float('-inf')
        for i in range(m - 1):
            if arrays[i][0] < second_min_val:
                second_min_val = arrays[i][0]
            if arrays[i][-1] > second_max_val:
                second_max_val = arrays[i][-1]

        return max(abs(max_val[0] - second_min_val), abs(second_max_val - min_val[0]))
        