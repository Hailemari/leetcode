# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -num)
            heappush(self.min_heap, -heappop(self.max_heap))
        else:
            heappush(self.min_heap, num)
            heappush(self.max_heap, -heappop(self.min_heap))
    
    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return self.min_heap[0]