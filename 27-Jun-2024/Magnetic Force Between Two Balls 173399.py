# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def canPlace(distance):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= distance:
                    count += 1
                    last = position[i]

                    if count == m:
                        return True

            return False
        

        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = left + (right - left) // 2
            if canPlace(mid):
                left = mid + 1
            else:
                right = mid - 1


        return right