# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        
        if nums[0] > target:
            return False

        used = [False] * len(nums)
        
        def backtrack(start, k, cur_sum):
            if k == 1:
                return True
            if cur_sum == target:
                return backtrack(0, k - 1, 0)
            
            for i in range(start, len(nums)):
                if not used[i] and cur_sum + nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, k, cur_sum + nums[i]):
                        return True
                    used[i] = False
            return False
        
        return backtrack(0, k, 0)