# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:
            stones.sort()
            l1 = stones.pop()
            l2 = stones.pop()

            if l1 != l2:
                stones.append(l1 - l2)


        if stones:
            return stones[0]
        
        return 0
