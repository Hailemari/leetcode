# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask_frequency = Counter({0: 1})
        wonderful_substrings_count = 0
        current_mask = 0

        for char in word:
            current_mask ^= 1 << (ord(char) - ord('a'))
            wonderful_substrings_count += mask_frequency[current_mask]

            for bit_shift in range(10):
                toggled_mask = current_mask ^ (1 << bit_shift)
                wonderful_substrings_count += mask_frequency[toggled_mask]

            mask_frequency[current_mask] += 1

        return wonderful_substrings_count