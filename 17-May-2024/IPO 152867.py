# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()

        min_heap = []
        max_heap = []

        for project in projects:
            heappush(min_heap, project)
        
        cur_capital = w

        for _ in range(k):
            while min_heap and min_heap[0][0] <= cur_capital:
                cap, pro = heappop(min_heap)
                heappush(max_heap, -pro)

            if not max_heap:
                break

            cur_capital += -heappop(max_heap)

        return cur_capital

