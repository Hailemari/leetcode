# Problem: Reach a Number - https://leetcode.com/problems/reach-a-number/

class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        steps = 0
        moves = 0

        while steps < target or (steps - target) % 2 != 0:
            moves += 1
            steps += moves

        return moves