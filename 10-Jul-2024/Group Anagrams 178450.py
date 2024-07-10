# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = defaultdict(list)

        for word in strs:
            new_word = tuple(sorted(word))
            sorted_strs[new_word].append(word)


        ans = []
        for val in sorted_strs.values():
            ans.append(val)

        return ans