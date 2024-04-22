# Problem: Delete Nodes And Return Forest - https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        if root.val not in to_delete:
            ans.append(root)
    
        def post_order(node):
            if node:
                if not node.left and not node.right:
                    if node.val in to_delete:
                        return True
                    return False

                if post_order(node.left):
                    node.left = None
                if post_order(node.right):
                    node.right = None

                if node.val in to_delete:
                    if node.left:
                        ans.append(node.left)
                    if node.right:
                        ans.append(node.right)

                    return True

                return False

        if root:
            post_order(root)

        return ans
        
