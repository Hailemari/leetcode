# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]

        if x > arr[-1]:
            return arr[len(arr) - k:]

        distance = defaultdict(int)
        for i, num in enumerate(arr):
            distance[(num, i)] = abs(num - x)
        
        heap = []
        heapify(heap)

        for key, val in distance.items():
            heappush(heap, (-val, -key[0]))
            if len(heap) > k:
                heappop(heap)

        ans = []
        while heap:
            ans.append(-heappop(heap)[1])

        ans = sorted(ans)
        return ans
        
