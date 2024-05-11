# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        def bits_to_string(bits, s):
            result = []
            for i, char in enumerate(s):
                if char.isalpha():
                    if bits & (1 << i):
                        result.append(char.upper())
                    else:
                        result.append(char.lower())
                else:
                    result.append(char)
            return "".join(result)

        result = set()
        n = len(s)
        for bits in range(2 ** n):
            result.add(bits_to_string(bits, s))

        return list(result)