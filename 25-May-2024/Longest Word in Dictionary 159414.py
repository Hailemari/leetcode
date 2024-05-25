# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        prefixes = set([""]) 
        ans = ""

        for word in words:
            if word[:-1] in prefixes:
                prefixes.add(word)
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans



