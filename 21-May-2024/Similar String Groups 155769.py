# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = {word: word for word in strs}
        rank = {word: 0 for word in strs}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]
            
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        def are_similar(a, b):
            if len(a) != len(b):
                return False
            diff = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append((a[i], b[i]))
                if len(diff) > 2:
                    return False
            return len(diff) == 2 and diff[0] == diff[1][::-1]

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if are_similar(strs[i], strs[j]):
                    union(strs[i], strs[j])
    
        return len({find(word) for word in strs})
