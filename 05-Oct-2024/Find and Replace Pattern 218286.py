# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def matches(word: str, pattern: str) -> bool:
            mapping = {}
            seen = set()

            for word_char, pattern_char in zip(word, pattern):
                if pattern_char in mapping:
                    if mapping[pattern_char] != word_char:
                        return False
                else:
                    if word_char in seen:
                        return False
                    mapping[pattern_char] = word_char
                    seen.add(word_char)

            return True

        return [word for word in words if matches(word, pattern)]
