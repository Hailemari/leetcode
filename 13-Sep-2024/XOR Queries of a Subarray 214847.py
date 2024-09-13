# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pre_sum = [arr[0]] * n

        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] ^ arr[i]

        ans = []
        for left, right in queries:
            if left > 0:
                ans.append(pre_sum[right] ^ pre_sum[left - 1])
            else:
                ans.append(pre_sum[right])

        return ans