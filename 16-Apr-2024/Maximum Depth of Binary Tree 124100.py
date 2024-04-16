# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def bfs(node, depth):
            if not node:
                return depth

            
            queue = deque([(node, depth + 1)])

            while queue:
                current, depth = queue.popleft()

                if current.left:
                    queue.append((current.left, depth + 1))
                if current.right:
                    queue.append((current.right, depth + 1))
        
            return depth

        return bfs(root, 0)