# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for key, val in count.items():
            if len(heap) < k:
                heappush(heap, (val, key))
            else:
                heappushpop(heap, (val, key))

        ans = []
        for key, val in heap:
            ans.append(val)

        return ans