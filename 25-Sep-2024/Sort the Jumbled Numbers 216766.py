# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def map_number(num):
            return int(''.join(str(mapping[int(c)]) for c in str(num)))

        return sorted(nums, key=lambda num: (map_number(num)))