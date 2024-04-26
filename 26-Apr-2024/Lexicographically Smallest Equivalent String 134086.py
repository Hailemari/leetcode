# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = {}
        rank = {}

        for char in set(s1 + s2 + baseStr):
            root[char] = char
            rank[char] = ord(char)

        def find(node):
            while node != root[node]:
                root[node] = root[root[node]]
                node = root[node]
            return node

        def union(node_a, node_b):
            root_a = find(node_a)
            root_b = find(node_b)

            if root_a != root_b:
                if rank[root_a] > rank[root_b]:
                    root[root_a] = root_b
                else:
                    root[root_b] = root_a
        
        for a, b in zip(s1, s2):
            union(a, b)

        equivalent_string = ""
        for c in baseStr:
            root_parent = find(c)
            equivalent_string += root_parent
        
        return equivalent_string


