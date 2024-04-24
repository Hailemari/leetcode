# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(len(heights) - 1):
            height_diff = heights[i+1] - heights[i]
            if height_diff > 0:
                heappush(heap, height_diff)
                if len(heap) > ladders:
                    bricks -= heappop(heap)
                if bricks < 0:
                    return i

        return len(heights) - 1            
