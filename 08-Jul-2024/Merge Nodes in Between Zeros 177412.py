# Problem: Merge Nodes in Between Zeros - https://leetcode.com/problems/merge-nodes-in-between-zeros

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = head
        cur_sum = 0
        temp = dummy
        while cur:
            new = cur.next
            if new:
                if new.val == 0:
                    temp.next = ListNode(cur_sum)
                    temp = temp.next
                    cur_sum = 0
                else:
                    cur_sum += new.val
        

                cur = cur.next
            else:
                break
        
        return dummy.next
