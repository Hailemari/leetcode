# Problem: Widest Vertical Area Between Two Points Containing No Points - https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        def comparator(point):
            return point[0]

        points.sort(key = comparator)
        widest_area = float('-inf')

        for i in range(len(points) - 1):
            widest_area = max(widest_area, points[i+1][0] - points[i][0])

        return widest_area
