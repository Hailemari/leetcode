# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        minHeap = []
        for i in range(len(heights) - 1):
            heightDiff = heights[i+1] - heights[i]
            if heightDiff > 0:
                heapq.heappush(minHeap, heightDiff)
                if len(minHeap) > ladders:
                    bricks -= heapq.heappop(minHeap)
                if bricks < 0:
                    return i

        return len(heights) - 1            

