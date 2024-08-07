# Problem: Minimum Number of Pushes to Type Word II - https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
    
        sorted_freq = sorted(freq.values(), reverse=True)
        
        total_pushes = 0
        for i, count in enumerate(sorted_freq):
            pushes = (i // 8) + 1
            total_pushes += count * pushes
        
        return total_pushes