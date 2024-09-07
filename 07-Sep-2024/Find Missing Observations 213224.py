# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_nums_sum = ((len(rolls) + n) * mean) - sum(rolls)
        
        res = []
        cur = n
        i = 6
        while i > 0 and cur > 0:
            if missing_nums_sum - i >= cur - 1:
                res.append(i)
                missing_nums_sum -= i
                cur -= 1
            else:
                i -= 1

        print(res)
        if len(res) == n and missing_nums_sum == 0:
            return res

        return []   

            
