# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        bit_masks = [] 
        for word in words:
            bitmask = 0
            for ch in set(word):
                bitmask |= 1 << (ord(ch) - ord('a'))

            bit_masks.append(bitmask)
            
        product = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if bit_masks[i] & bit_masks[j] == 0:
                    product = max(product, len(words[i]) * len(words[j]))

        return product