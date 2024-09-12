# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_freq = Counter(allowed)
        
        count = 0
        for word in words:
            word_freq = Counter(word)
            
            flag = True
            for char, freq in word_freq.items():
                if allowed_freq.get(char, 0) == 0:
                    flag = False
                    break
            
            if flag:
                count += 1


        return count


