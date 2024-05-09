# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def f(i, memo):
            if i == 0:
                return nums[i]
            if i < 0:
                return 0
        
            if i in memo:
                return memo[i]
            
            take = nums[i] + f(i - 2, memo)
            not_take = f(i - 1, memo)

            memo[i] = max(take, not_take)
            return memo[i]


        return f(n - 1, {})
        