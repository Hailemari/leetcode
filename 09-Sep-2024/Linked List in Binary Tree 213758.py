# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(node, head):
            if not head:
                return True
            if not node:
                return False

            if node.val == head.val:
                return dfs(node.left, head.next) or dfs(node.right, head.next)

            return False


        def traverse(root):
            if not root:
                return False
            
            if dfs(root, head):
                return True

            return traverse(root.left) or traverse(root.right)
        
        return traverse(root)
