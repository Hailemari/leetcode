# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]  
            
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)
            
            good_pairs = 0
            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        good_pairs += 1
            
            current_distances = []
            for ld in left_distances:
                current_distances.append(ld + 1)
            for rd in right_distances:
                current_distances.append(rd + 1)
            
            nonlocal result
            result += good_pairs
            return current_distances
        
        result = 0
        dfs(root)
        return result