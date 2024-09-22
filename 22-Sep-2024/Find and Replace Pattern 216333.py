# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def matches(word: str, pattern: str) -> bool:
            mapping = {}
            seen = set()

            for w_char, p_char in zip(word, pattern):
                if p_char in mapping:
                    if mapping[p_char] != w_char:
                        return False
                else:
                    if w_char in seen:
                        return False
                    mapping[p_char] = w_char
                    seen.add(w_char)

            return True

        return [word for word in words if matches(word, pattern)]
