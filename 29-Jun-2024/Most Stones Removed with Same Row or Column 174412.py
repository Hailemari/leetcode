# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {(a, b): (a, b) for a, b in stones}
        rank = {(a, b): 0 for a, b in stones}

        def find(coordinate):
            if parent[coordinate] != coordinate:
                parent[coordinate] = find(parent[coordinate])

            return parent[coordinate]

        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)

            if parent_a != parent_b:
                if rank[parent_a] > rank[parent_b]:
                    parent[parent_b] = parent_a

                elif rank[parent_a] < rank[parent_b]:
                    parent[parent_a] = parent_b
                
                else:
                    parent[parent_a] = parent_b
                    rank[parent_b] += 1

            
        for i in range(len(stones)):
            a, b = stones[i]
            for j in range(i + 1, len(stones)):
                c, d = stones[j]

                if a == c or b == d:
                    union((a, b), (c, d))

        
        unique_parents = set()
        for a, b in stones:
            unique_parents.add(find((a, b)))

      
        return len(stones) - len(unique_parents)