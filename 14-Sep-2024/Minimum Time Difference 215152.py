# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        timePoints.sort()
        
        min_time = float('inf')

        for i in range(1, n):
            prev_hour = int(timePoints[i - 1][:2])
            prev_minute = int(timePoints[i - 1][3:])
            
            cur_hour = int(timePoints[i][:2])
            cur_minute = int(timePoints[i][3:])


            min_time = min(min_time, (cur_hour - prev_hour)*60 + (cur_minute - prev_minute))

        prev_hour = int(timePoints[n - 1][:2])
        prev_minute = int(timePoints[n - 1][3:])
        
        temp = ((24 - prev_hour) * 60) - prev_minute + (int(timePoints[0][:2]) * 60 + int(timePoints[0][3:]))
        
        min_time = min(min_time, temp)
        
        return min_time

        