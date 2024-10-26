# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        max_width = 0
        level_nodes = deque([(root, 0)])

        while level_nodes:
            current_level_length = len(level_nodes)
            first_position = level_nodes[0][1] 

            for _ in range(current_level_length):
                current_node, current_position = level_nodes.popleft()

                if current_node.left:
                    level_nodes.append((current_node.left, 2 * current_position))
                if current_node.right:
                    level_nodes.append((current_node.right, 2 * current_position + 1))

            last_position = current_position
            level_width = last_position - first_position + 1
            max_width = max(max_width, level_width)

        return max_width
