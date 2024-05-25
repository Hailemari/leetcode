# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, number: int) -> None:
        node = self.root
        for i in range(31, -1, -1):
            bit = (number >> i) & 1
            if node.children[bit] is None:
                node.children[bit] = TrieNode()
            node = node.children[bit]

class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        trie = Trie()
        for num in nums:
            trie.add(num)
        
        max_xor = 0
        for num in nums:
            node = trie.root
            current_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opposite_bit = 1 - bit
                if node.children[opposite_bit] is not None:
                    current_xor = (current_xor << 1) | 1
                    node = node.children[opposite_bit]
                else:
                    current_xor = (current_xor << 1)
                    node = node.children[bit]
            max_xor = max(max_xor, current_xor)
        
        return max_xor
