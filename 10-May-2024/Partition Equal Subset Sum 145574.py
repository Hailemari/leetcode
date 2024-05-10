# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2:
            return False

        n = len(nums)
        target = total_sum // 2

        def f(i, arr, target, memo):
            if target == 0:
                return True
            if i < 0 or target < 0:
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = f(i - 1, arr, target - arr[i], memo) or f(i - 1, arr, target, memo)
                
            return memo[(i, target)]
            
        return f(n - 1, nums, target, {})