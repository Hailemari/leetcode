# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            l1 = -heapq.heappop(stones)
            l2 = -heapq.heappop(stones)

            if l1 != l2:
                heapq.heappush(stones, l2 - l1)

        if stones:
            return -stones[0]

        return 0