# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
    
        def backtrack(substring, index):
            if index == len(s):
                result.append(substring)
                return
            
            if s[index].isdigit():
                backtrack(substring + s[index], index + 1)
            else:
                backtrack(substring + s[index].lower(), index + 1)
                backtrack(substring + s[index].upper(), index + 1)
        
        backtrack("", 0)
        return result