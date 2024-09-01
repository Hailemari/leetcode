# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        ans = []
        for val in anagrams.values():
            ans.append(val)

        return ans