# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        
        max_profit = 0
        max_profit_at_difficulty = []
        
        for d, p in jobs:
            max_profit = max(max_profit, p)
            max_profit_at_difficulty.append((d, max_profit))
        
        def find_max_profit(ability):
            left, right = 0, len(max_profit_at_difficulty) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if max_profit_at_difficulty[mid][0] <= ability:
                    left = mid + 1
                else:
                    right = mid - 1
            return max_profit_at_difficulty[right][1] if right >= 0 else 0
        
        worker.sort()
        total_profit = 0
        
        for ability in worker:
            total_profit += find_max_profit(ability)
        
        return total_profit