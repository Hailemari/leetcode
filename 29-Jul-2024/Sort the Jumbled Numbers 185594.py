# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = []

        for idx, num in enumerate(nums):
            num_str = str(num)
            new_num = ""
            for c in num_str:
                new_num += str(mapping[int(c)])

            new_nums.append((int(new_num), idx, num))

        
        new_nums.sort(key = lambda x : (x[0], x[1]))

        ans = []
        for new_num, _ , num in new_nums:
            ans.append(num)

        return ans
