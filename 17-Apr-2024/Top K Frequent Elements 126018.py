# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        count = dict(sorted(count.items(), key = lambda x: -x[1]))

        ans = []
        
        for key in count.keys():
            if k:
                ans.append(key)
                k -= 1
            else:
                break

        return ans