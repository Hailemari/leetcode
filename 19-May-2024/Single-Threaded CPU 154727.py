# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = [(enqueue_time, processing_time, index) for index, (enqueue_time, processing_time) in enumerate(tasks)]

        indexed_tasks.sort()

        min_heap = []
        time = 0
        i = 0

        result = []
        while i < len(indexed_tasks) or min_heap:
            while i < len(indexed_tasks) and indexed_tasks[i][0] <= time:
                heappush(min_heap, (indexed_tasks[i][1], indexed_tasks[i][2]))
                i += 1

            if min_heap:
                processing_time, index = heappop(min_heap)
                time += processing_time
                result.append(index)

            else:
                time = indexed_tasks[i][0]

        return result