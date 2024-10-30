# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, path_sum):
            if node is None:
                return 0

            # Update the path sum as we traverse down the tree
            path_sum = path_sum * 10 + node.val

            # Check if we've reached a leaf node
            if node.left is None and node.right is None:
                return path_sum

            # Recur for both subtrees and add their results
            left_sum = dfs(node.left, path_sum)
            right_sum = dfs(node.right, path_sum)
            return left_sum + right_sum

        return dfs(root, 0)
