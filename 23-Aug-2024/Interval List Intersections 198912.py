# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)

        ans = []
        while i < n and j < m:
            start_i = firstList[i][0]
            start_j = secondList[j][0]
            end_i = firstList[i][1]
            end_j = secondList[j][1]

            x = max(start_i, start_j)
            y = min(end_i, end_j)

            if x <= y:
                ans.append([x, y])
                if end_i < end_j:
                    i += 1
                else:
                    j += 1
            else:
                if end_i < end_j:
                    i += 1
                else:
                    j += 1

        return ans


