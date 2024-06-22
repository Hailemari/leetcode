# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        res = 0
        n = len(nums1)
        for i in range(n):
            cur = bisect_right(arr , nums1[i] - nums2[i] + diff)
            res += cur
            bisect.insort(arr , nums1[i] - nums2[i])

        return res