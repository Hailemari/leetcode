# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def buildGraph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                buildGraph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                buildGraph(node.right)
        
        buildGraph(root)
        
        def bfs(node, target_dis, cur_dis):
            queue = deque([(node, cur_dis)])
            
            visited = {node}
            ans = []
            while queue:
                cur, cur_dis = queue.popleft()
                if cur_dis == target_dis:
                    ans.append(cur)

                for node in graph[cur]:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, cur_dis + 1))


            return ans
        ans = []
        for node in graph.keys():
            if node == target.val:
                ans = bfs(node, k, 0)

        return ans