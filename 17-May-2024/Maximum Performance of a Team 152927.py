# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        teams = list(zip(efficiency, speed))
        teams.sort(reverse = True)

        min_heap = []
        max_performance, tot_speed = 0, 0
        for eff, cur_speed in teams:
            if len(min_heap) == k:
                tot_speed -= heappop(min_heap)

            tot_speed += cur_speed
            heappush(min_heap, cur_speed)
            max_performance = max(max_performance, eff * (tot_speed))
       

        return max_performance % (10 ** 9 + 7)