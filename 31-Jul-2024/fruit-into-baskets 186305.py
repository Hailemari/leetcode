# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruit = float('-inf')
        n = len(fruits)
        types = {}
        l = 0

        for r in range(n):
            types[fruits[r]] = types.get(fruits[r], 0) + 1

            while len(types) > 2:
                types[fruits[l]] -= 1
                if types[fruits[l]] == 0:
                    del types[fruits[l]]

                l += 1

            max_fruit = max(max_fruit, r - l + 1)

        return max_fruit

            

            

            
