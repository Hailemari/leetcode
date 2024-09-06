# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            pattern_freq = {}
            mapped = set()
            Flag = True
            for char1, char2 in zip(word, pattern):
                val = pattern_freq.get(char2, "")
                if val != "":
                    if val != char1:
                        Flag = False
                        break
                else:
                    pattern_freq[char2] = char1
                    if char1 in mapped:
                        Flag = False
                        break
                    mapped.add(char1)

            if Flag:
                ans.append(word)

        return ans