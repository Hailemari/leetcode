# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        levels = []
        level = [root]

        while level:
            if level:
                levels.append(level)

            current = []
            for node in level:
                if node.left:
                    current.append(node.left)
                if node.right:
                    current.append(node.right)

            level = current

        ans = []
        for level in levels:
            cur_sum = sum([node.val for node in level]) / len(level)
            ans.append(cur_sum)

        return ans