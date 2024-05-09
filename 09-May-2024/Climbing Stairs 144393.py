# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        def memoized(ind, memo):
            if ind == 0:
                return 1
            if ind < 0:
                return 0
            
            if ind in memo:
                return memo[ind]
            
            one_step = memoized(ind - 1, memo)
            two_step = memoized(ind - 2, memo)

            memo[ind] = one_step + two_step
            return memo[ind]

        return memoized(n, {})