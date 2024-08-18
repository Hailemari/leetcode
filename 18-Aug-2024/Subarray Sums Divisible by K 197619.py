# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_freq = {}
        answer = 0

        for pref_sum in accumulate(nums):
            pref_sum %= k
            if pref_sum == 0:
                answer += 1

            if pref_sum in remainder_freq:
                answer += remainder_freq[pref_sum]

            remainder_freq[pref_sum] = remainder_freq.get(pref_sum, 0) + 1

        return answer