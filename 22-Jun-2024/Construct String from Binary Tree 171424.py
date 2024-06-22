# Problem: Construct String from Binary Tree - https://leetcode.com/problems/construct-string-from-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: TreeNode) -> str:
        def dfs(node):
            if not node:
                return ""
            
            left_str = dfs(node.left)
            right_str = dfs(node.right)

            result = str(node.val)

            if left_str or right_str:
                result += f"({left_str})"
            
            if right_str:
                result += f"({right_str})"

            return result
        
        return dfs(root)
            
