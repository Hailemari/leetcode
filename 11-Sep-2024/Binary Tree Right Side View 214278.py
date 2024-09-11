# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        right_side = [] 
        
        while queue:
            level_length = len(queue)
       
            for i in range(level_length):
                node = queue.popleft()
                
                if i == level_length - 1:
                    right_side.append(node.val)
                

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_side

        