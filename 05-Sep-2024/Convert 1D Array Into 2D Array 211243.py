# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        for i in range(0, len(original), n):
            ans.append(original[i:i+n])

        if len(ans) != m or len(ans[0]) != n:
            return []

        return ans