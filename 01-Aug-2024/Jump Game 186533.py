# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        
        for j in range(n - 1):
            if nums[j] == 0:
                Flag = False
                while i < j:
                    if nums[i] + i > j:
                        Flag = True
                        break
                    i += 1
                
                if not Flag:
                    return False

        return True

                    



        