# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        ans = []
        def f(node):
            if node and len((node.children)) == 0:
                ans.append(node.val)
                return
            
            if node != None:
                for n in node.children:
                    if n != None:
                        f(n)
            
                ans.append(node.val)

        f(root)
        return ans
        