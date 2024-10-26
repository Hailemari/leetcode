# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = [] 

        for current in range(len(heights) - 1):
            climb = heights[current + 1] - heights[current]

            if climb > 0:
                heapq.heappush(min_heap, climb)

                if len(min_heap) > ladders:
                    bricks -= heapq.heappop(min_heap)

                if bricks < 0:
                    return current

        return len(heights) - 1