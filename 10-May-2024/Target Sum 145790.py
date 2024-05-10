# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        
        def f(i, target, memo):
            if i < 0:
                if target == 0:
                    return 1
                else:
                    return 0
            
            if (i, target) in memo:
                return memo[(i, target)]

            left = f(i - 1, target - nums[i], memo)
            right = f(i - 1, target + nums[i], memo)

            memo[(i, target)] = left + right
            return memo[(i, target)]
            
        return f(n, target, {})