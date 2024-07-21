# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = deque()

        level.append(root)

        res = []
        while level:
            count = False
            n = len(level)
            for i in range(n - 1, -1, -1):
                if level[i]:
                    count = True
                    res.append(level[i].val)
                    break

            if not count:
                break
                
            cur = deque()
            while level:
                node = level.popleft()
                if node:
                    cur.append(node.left)
                    cur.append(node.right)

            level = cur

        return res

        