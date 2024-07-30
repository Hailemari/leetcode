# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)
        
        def build_graph(node, parent=None):
            if node:
                if parent:
                    graph[node.val].append((parent.val, 'U'))
                    graph[parent.val].append((node.val, 'L' if node == parent.left else 'R'))
                if node.left:
                    build_graph(node.left, node)
                if node.right:
                    build_graph(node.right, node)
        
        build_graph(root)
        
        def find_path(src, dst):
            queue = [(src, "")]
            visited = set()
            
            while queue:
                node, path = queue.pop(0)
                
                if node == dst:
                    return path
                
                visited.add(node)
                
                for neighbor, direction in graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + direction))
            
            return ""
        
        return find_path(startValue, destValue)

        
        def dfs(node):
            if not node:
                return

            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)
            
            dfs(node.left)
            dfs(node.right)

        dfs(root)
    
        def find_path(src, path, dis):
            visited = set([src])
           
            l, r, u = graph[src]
            if l == destValue:
                return shortest_path + "L", dis
            if r == destValue:
                return path + "R", dis
            if u == destValue:
                return path + "U", dis
            
            dis += 1
            if l and l not in visited:
                find_path(l, path + "L", dis)
            if r and r not in visited:
                find_path(r, path + "R", dis)
            if u and u not in visited:
                find_path(u, path + "U", dis)

        print(graph)
        
        l, r, u = graph[startValue]
        left_dis, right_dis, up_dis = float('inf'), float('inf'), float('inf')
        if l:
            left, left_dis = find_path(l, "L", 1)
        if r:
            right, right_dis = find_path(r, "R", 1)
        if u:
            up, up_dis = find_path(u, "U", 1)

        min_dis = min(left_dis, right_dis, up_dis)
        if min_dis == left_dis:
            return left
        elif min_dis == right_dis:
            return right
        else:
            return up