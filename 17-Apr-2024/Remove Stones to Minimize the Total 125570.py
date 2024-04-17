# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]

        heapify(piles)

        while k:
            max_num = -heappop(piles)
            heappush(piles, (floor(max_num / 2) - max_num))
            k -= 1
    
        return -sum(piles)