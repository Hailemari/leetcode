# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = nums[i] * -1

        heapify(nums)

        while k > 1:
            heappop(nums)
            k -= 1

        return nums[0] * -1