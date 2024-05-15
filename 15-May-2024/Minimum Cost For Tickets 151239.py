# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        def f(i, passes, memo):
            if i == n:
                return 0
            if (i, passes) in memo:
                return memo[(i, passes)] 
            if passes > days[i]:
                return f(i + 1, passes, memo)

            min_val = float('inf')
           
            for cost, val in zip(costs, [1, 7, 30]):
                min_val = min(min_val, cost + f(i + 1, days[i] + val, memo))
          
            memo[(i, passes)] = min_val
            return memo[(i, passes)]
        return f(0, 0, {})