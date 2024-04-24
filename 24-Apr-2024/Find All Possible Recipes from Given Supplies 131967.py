# Problem: Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        graph = {}
        indegree = {key: 0 for key in recipes}
        indexes = {}
        

        for idx, recipe in enumerate(recipes):
            graph[recipe] = []
            indexes[recipe] = idx

        for i in range(n):
            for recipe in recipes:
                if recipe in ingredients[i]:
                    graph[recipe].append(recipes[i])
                    indegree[recipes[i]] += 1


        queue = deque()
        for key, val in indegree.items():
            Flag = True
            if val == 0:
                for ing in ingredients[indexes[key]]:
                    if ing not in supplies:
                        Flag = False
                if Flag:
                    queue.append(key)
                    supplies.append(key)

        order = []
        while queue:
            cur = queue.popleft()
            order.append(cur)

            for neighbor in graph[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    print(neighbor)
                    queue.append(neighbor)

        

        return order

        
